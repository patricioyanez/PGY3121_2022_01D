from . import views
from django.urls import path

urlpatterns = [
    path('categoria', views.categoria , name='categoria'),
    ]