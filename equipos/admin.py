from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'memoria_ram', 'almacenamiento', 'monitor', 'raton', 'sistema_operativo', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre',)
