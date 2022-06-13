from . import views
from django.urls import path

urlpatterns = [
    path('categoria', views.categoria , name='categoria'),
    path('categoria/<int:buscarId>/', views.categoriaLeer , name='categoria1'),
    path('ApiCategoria', views.ApiCategoria , name='ApiCategoria'),

    path('crudMarca', views.marca , name='marca'),
    ]
    # crud => esta definido en   el urls del proyecto base (proyecto1 urls.py)
    # 127.0.0.1:8000/crud/categoria