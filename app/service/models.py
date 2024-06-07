from django.db import models

# Create your models here.

class QueryHistory(models.Model):
    cadastral_number = models.CharField(max_length=255,verbose_name="Кадастровый номер")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    result = models.BooleanField(verbose_name="Результат")
    query_time = models.DateTimeField(auto_now_add=True,verbose_name="Время отправки запроса")

    class Meta:
        verbose_name = "Кадастровая информация"
        verbose_name_plural = "Кадастровая информация"
