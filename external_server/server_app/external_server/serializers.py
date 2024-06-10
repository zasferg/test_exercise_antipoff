from rest_framework import serializers
from .models import ExrernalServerCadastral


class ExternalServerCadastralSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExrernalServerCadastral
        fields = '__all__'
