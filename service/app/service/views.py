
from rest_framework import status 
from rest_framework.decorators import api_view
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

# Это IP внешнего сервера, которое находится в контейнере externall_app
EXTERNAL_SERVER_URL = "http://172.19.0.3:8001"


class QueryPoint(APIView):
    """Здесь мы отправляем данные на внешний сервер. Внешним сервером у нас является приложение в контейнере external_app.
    Так же добавляется запись о запросе в инсторию запросов"""
    def post(self, request: Request)-> Response:
        if not request.data:
            return Response({"message": "Нет данных в запросе"}, status=status.HTTP_400_BAD_REQUEST)
        response = requests.post(url=f"{EXTERNAL_SERVER_URL}/server/",data=request.data)
        message = response.json()
        request.data["result"] = message["message"]
        serializer = QuerySerializer(data=request.data)
        history_serializer = HistorySerializer(data={"cadastral_number":request.data["cadastral_number"],
                                                     "query_date" : request.data["query_time"],
                                                     "response_status":response.status_code,
                                                     "result":message["message"],
                                                     })
        if serializer.is_valid() and history_serializer.is_valid():
            serializer.save()
            history_serializer.save()
            return Response({"message": "Ответ сeрвера:"f'{serializer.data["result"]}'},status=status.HTTP_200_OK)

class PingPoint(APIView):
    """Здесь мы тестируем пинг нашего внешнего сервера"""
    def get(self,request:Request) -> Response:
        try:
            response = requests.get(url=f"{EXTERNAL_SERVER_URL}/server/",timeout=60).status_code
            if response < 500: 
                return Response({"status": "Сервер работает"}, status=response)
            else: 
                return Response({"status": "Сервер не работает"}, status=response)
        except requests.exceptions.Timeout:                                
            return Response({'message': 'Время ожидания истекло'})             


class ResultPoint(APIView):
    """Здесь мы получаем данные по кадастровому номеру """
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
    """Зесь мы получаем историю апросов"""
    def get(self, request, cad_num, format=None):
        if not cad_num:
            return Response({"error": "Пустой кадастровый номер"}, status=status.HTTP_400_BAD_REQUEST)

        queries = QueryHistory.objects.filter(cadastral_number=cad_num)
        
        if not queries.exists():
            return Response({"error": "Для этого кадастрового нмера нет истории запросов"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HistorySerializer(queries, many=True)
        return Response(serializer.data)

