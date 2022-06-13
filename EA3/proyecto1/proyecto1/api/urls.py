from django.urls import path

from api.views import apiCategoria, apiCategoriaDetalle

urlpatterns = [
    path('apiCategoria', apiCategoria, name="apiCategoria"),
    path('apiCategoriaDetalle/<buscarId>/', apiCategoriaDetalle, name="apiCategoriaDetalle"),
]