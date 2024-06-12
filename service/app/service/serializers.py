from rest_framework import serializers
from .models import QueryHistory
from .models import Cadastral

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastral
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryHistory
        fields = '__all__'


