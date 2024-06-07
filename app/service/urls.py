from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import QueryPoint
from .views import PingPoint
from .views import ResultPoint
from .views import HistoryPoint

# query_router = DefaultRouter()
# query_router.register(r'query', QueryPoint,basename='query')



urlpatterns = [
    path('query/', QueryPoint.as_view(), name='query'),
    path('result/<int:query_id>/', ResultPoint.as_view(), name='result'),
    path('ping/', PingPoint.as_view(), name='ping'),
    path('history/<str:cad_num>/', HistoryPoint.as_view(), name='history'),
]