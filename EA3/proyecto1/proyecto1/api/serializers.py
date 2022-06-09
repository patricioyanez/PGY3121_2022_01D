from rest_framework import serializers
from crud.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Categoria
        fields  = ['nombre', 'activo'] # __all__