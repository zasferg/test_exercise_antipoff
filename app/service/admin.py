from django.contrib import admin
from .models import QueryHistory
from .models import Cadastral
# Register your models here.

@admin.register(Cadastral)
class QueryHistoryAdmin(admin.ModelAdmin):
    list_display = ("cadastral_number","latitude","longitude","query_time","result")
    list_filter = ("cadastral_number",)
    search_fields = ("cadastral_number__startswith",)


@admin.register(QueryHistory)
class QueryHistoryAdmin(admin.ModelAdmin):
    list_display = ('query_date', 'query_data', 'response_status', 'response_data')
    list_filter = ("cadastral_number",)
    search_fields = ("cadastral_number__startswith",)



