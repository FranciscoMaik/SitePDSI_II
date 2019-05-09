from django.urls import path
from . import views


urlpatterns = [
    path('', views.funcio, name='Funcio'),
]
