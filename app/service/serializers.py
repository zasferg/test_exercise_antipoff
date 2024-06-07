from rest_framework import serializers
from .models import QueryHistory

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryHistory
        fields = '__all__'

