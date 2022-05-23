from django.contrib import admin
from .models import Marca, Categoria

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter  = ['nombre']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter  = ['nombre', 'activo']

# Register your models here.
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
