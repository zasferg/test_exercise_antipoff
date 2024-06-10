from rest_framework import serializers
from .models import QueryHistory

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryHistory
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryHistory
        fields = ['query_date', 'query_data', 'response_status', 'response_data']


