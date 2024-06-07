from django.shortcuts import render
from rest_framework import status
from .models import QueryHistory
from .serializers import QuerySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from random import randint,choice
import requests

from time import sleep

class QueryPoint(APIView):

    @staticmethod
    def emulate_external_request():
        sleep(randint(1, 60))
    
    def post(self, request):
        serializer = QuerySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            self.emulate_external_request()
            return Response({"message": "Запрос отправлен"},status=status.HTTP_200_OK)
        return Response({"message": "Произошла ошибка"}, status=status.HTTP_400_BAD_REQUEST)


class ResultPoint(APIView):

    def get_object(self,query_id):
        try:
            return QueryHistory.objects.get(pk=query_id)
        except QueryHistory.DoesNotExist:
            return Response({"message": 'False'},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,query_id):
        some_query = self.get_object(query_id)
        return Response({"result_field":some_query.result},status=status.HTTP_200_OK)


class PingPoint(APIView):
    @staticmethod
    def get_api_response():
        return requests.get('http://127.0.0.1:8000/openapi').status_code

    def get(self, format=None):
        print(self.get_api_response())
        if not self.get_api_response() > 500 : 
            return Response({"status": "Сервер работает"}, status=self.get_api_response())
        else: 
            return Response({"status": "Сервер не работает"}, status=self.get_api_response())


    
class HistoryPoint(APIView):

    def get_object(self,cad_number):
        try:
            return QueryHistory.objects.filter(cadastral_number=cad_number)
        except QueryHistory.DoesNotExist:
            return Response({"message": 'Данной записи не существует'},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,cad_num):
        some_query = self.get_object(cad_num)
        serializer = QuerySerializer(some_query, many=True)
        return Response(serializer.data)


        







