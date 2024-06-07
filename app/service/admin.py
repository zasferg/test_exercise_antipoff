from django.contrib import admin
from .models import QueryHistory
# Register your models here.

@admin.register(QueryHistory)
class QueryHistoryAdmin(admin.ModelAdmin):
    list_display = ("cadastral_number","latitude","longitude","query_time","result")
    list_filter = ("cadastral_number",)
    search_fields = ("cadastral_number__startswith",)



