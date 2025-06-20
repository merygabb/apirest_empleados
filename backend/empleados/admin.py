
# regitra modelos al administrador de Django
from django.contrib import admin
from .models import Empleado
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'estado')
    search_fields = ('codigo', 'nombre')
    list_filter = ('estado',)
    ordering = ('codigo',)
    fieldsets = (
        (None, {
            'fields': ('codigo', 'nombre', 'estado')
        }),
    )