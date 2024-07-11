from django.contrib import admin
from .models import ExrernalServerCadastral


# Register your models here.
@admin.register(ExrernalServerCadastral)
class QueryHistoryAdmin(admin.ModelAdmin):
    list_display = ("cadastral_number", "latitude", "longitude", "query_time")
    list_filter = ("cadastral_number",)
    search_fields = ("cadastral_number__startswith",)
