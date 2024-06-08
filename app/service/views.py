
from rest_framework import status
from rest_framework import generics
from .models import QueryHistory
from .models import Cadastral
from .serializers import QuerySerializer
from .serializers import HistorySerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from random import randint,choice
import requests
import os
from typing import List, Union
from time import sleep




class QueryPoint(APIView):
    @staticmethod
    def emulate_external_request() -> None:
        sleep(randint(1, 60))
    
    def post(self, request: Request) -> Response:
        if not request.data:
            return Response({"message": "Нет данных в запросе"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.emulate_external_request()
            return Response({"message": "Запрос отправлен"},status=status.HTTP_200_OK)
        return Response({"message": "Произошла ошибка", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PingPoint(APIView):
    @staticmethod
    def get_api_response() -> int:
        return requests.get('http://127.0.0.1:8000/openapi').status_code

    def get(self, format=None) -> Response:
        if not self.get_api_response() > 500 : 
            return Response({"status": "Сервер работает"}, status=self.get_api_response())
        else: 
            return Response({"status": "Сервер не работает"}, status=self.get_api_response())

class ResultPoint(APIView):
    def get_object(self,cad_number: str) -> Union[Response, QueryHistory]:
        try:
            return Cadastral.objects.filter(cadastral_number=cad_number)
        except Cadastral.DoesNotExist:
            return Response({"message": 'Данной записи не существует'},status=status.HTTP_404_NOT_FOUND)

    def get(self,request: Request, cad_num: str) -> Response:
        some_query = self.get_object(cad_num)
        serializer = QuerySerializer(some_query, many=True)
        return Response(serializer.data)

class HistoryPoint(APIView):

    def get(self, request, cad_num, format=None):
        if not cad_num:
            return Response({"error": "Пустой кадастровый номер"}, status=status.HTTP_400_BAD_REQUEST)

        queries = QueryHistory.objects.filter(cadastral_number=cad_num)
        
        if not queries.exists():
            return Response({"error": "Для этого кадастрового нмера нет истории запросов"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HistorySerializer(queries, many=True)
        return Response(serializer.data)

