
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

EXTERNAL_SERVER_URL = "http://127.0.0.1:8001"


class QueryPoint(APIView):

    def post(self, request: Request) -> Response:
        if not request.data:
            return Response({"message": "Нет данных в запросе"}, status=status.HTTP_400_BAD_REQUEST)
        

        response = requests.post(url="http://127.0.0.1:8001/server/",data=request.data)
        message = response.json()
        print(message)
        request.data["result"] = message["status"]
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Запрос отправлен"},status=status.HTTP_200_OK)
        return Response({"message": "Произошла ошибка", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

# class PingPoint(APIView):
#     def get(self,request:Request) -> int:
#             response = requests.get(url="http://127.0.0.1:8001/",timeout=60).status_code
#             if response < 500: 
#                 return Response({"status": "Сервер работает"}, status=response)
#             else: 
#                 return Response({"status": "Сервер не работает"}, status=response)
#         # except requests.exceptions.Timeout:                                
#         #     return Response({'message': 'Время ожидания истекло'})             

# def get_response():
#     response = requests.get(url="http://external_app:8000/",timeout=60)
#     print(response)
#     return response

response = requests.get(url="http://127.0.0.1:8001/server/")
@api_view(['GET'])
def PingPoint(request):
    if request.method == 'GET':
        if response.status_code < 500: 
            return Response({"status": "Сервер работает"}, status=response.status_code)
        else: 
            return Response({"status": "Сервер не работает"}, status=response.status_code)

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

