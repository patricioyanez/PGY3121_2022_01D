from django.urls import path

from api.views import apiCategoria

urlpatterns = [
    path('apiCategoria', apiCategoria, name="apiCategoria")
]