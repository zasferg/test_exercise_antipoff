from django.urls import include, path

from .views import ExternalServerPoint



urlpatterns = [
    path('server/', ExternalServerPoint.as_view(), name='server'),
]