from django.shortcuts import render
from requests import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ExternalServerCadastralSerializer
from .models import  ExrernalServerCadastral
# Create your views here.

class ExternalServerPoint(APIView):
    def post(self,request):
        print(request.data)
        serializer = ExternalServerCadastralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data":request.data,"status":"true"},status=status.HTTP_201_CREATED)