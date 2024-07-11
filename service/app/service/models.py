import datetime
from django.db import models

# Create your models here.


class Cadastral(models.Model):
    cadastral_number = models.CharField(
        max_length=255, verbose_name="Кадастровый номер"
    )
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.CharField(verbose_name="Долгота")
    result = models.BooleanField(verbose_name="Результат")
    query_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Время отправки запроса"
    )

    class Meta:
        verbose_name = "Кадастровая информация"
        verbose_name_plural = "Кадастровая информация"


class QueryHistory(models.Model):
    cadastral_number = models.CharField(
        max_length=100, verbose_name="Кадастровый номер"
    )
    query_date = models.DateTimeField(
        default=datetime.datetime.now().isoformat(), verbose_name="Дата запроса"
    )
    response_status = models.IntegerField(null=True, verbose_name="Статус ответа")
    result = models.BooleanField(null=True, verbose_name="Результат ответа")

    class Meta:
        verbose_name = "История запросов"
        verbose_name_plural = "История запросов"
