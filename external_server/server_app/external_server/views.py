from django.shortcuts import render
from requests import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ExternalServerCadastralSerializer
from .models import  ExrernalServerCadastral
# Create your views here.
from django.http import HttpResponse
import json



class ExternalServerPoint(APIView):
    def post(self,request):
        """Здесь мы принимаем данные из нашего приложения и отправлем результат"""
        try:
            serializer = ExternalServerCadastralSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return HttpResponse(json.dumps({"message":True, "data":serializer.data}), status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))
            return HttpResponse(json.dumps({"message":False,"exception":f"{str(e)}"}), status=status.HTTP_201_CREATED)
