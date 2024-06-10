import datetime
from django.db import models

# Create your models here.

class Cadastral(models.Model):
    cadastral_number = models.CharField(max_length=255,verbose_name="Кадастровый номер")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.CharField(verbose_name="Долгота")
    result = models.CharField(verbose_name="Результат")
    query_time = models.DateTimeField(auto_now_add=True,verbose_name="Время отправки запроса")

    class Meta:
        verbose_name = "Кадастровая информация"
        verbose_name_plural = "Кадастровая информация"


class QueryHistory(models.Model):
    cadastral_number = models.CharField(max_length=100,verbose_name="Кадастровый номер")
    query_date = models.DateTimeField(default=datetime.datetime.now().isoformat(),verbose_name="Дата запроса")
    query_data = models.CharField(max_length=100,null=True,verbose_name="Данные запроса")
    response_status = models.BooleanField(null=True,verbose_name="Статус ответа")
    response_data = models.CharField(max_length=100,null=True,verbose_name="Данные ответа")
    

    class Meta:
        verbose_name = "История запросов"
        verbose_name_plural = "История запросов"

    def __str__(self):
        return self.cadastral_number

