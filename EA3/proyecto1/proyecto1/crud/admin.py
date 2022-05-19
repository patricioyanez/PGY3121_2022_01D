from django.contrib import admin
from .models import Marca

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter  = ['nombre']


# Register your models here.
admin.site.register(Marca, MarcaAdmin)
