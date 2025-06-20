from .models import Empleado
from rest_framework import serializers
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'codigo', 'nombre', 'estado']
        read_only_fields = ['id']
        