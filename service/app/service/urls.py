from django.urls import include, path

from .views import QueryPoint
from .views import PingPoint
from .views import ResultPoint
from .views import HistoryPoint



urlpatterns = [
    path('query/', QueryPoint.as_view(), name='query'),
    path('result/<str:cad_num>/', ResultPoint.as_view(), name='result'),
    path('ping/', PingPoint.as_view(), name='ping'),
    path('history/<str:cad_num>/', HistoryPoint.as_view(), name='history'),
]