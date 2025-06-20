from django.urls import path, include
from .api import EmpleadoListAPIView, TotalEmpleadosAPIView, AddEmpleadoAPIView

urlpatterns = [
    path('lista-empleados/', EmpleadoListAPIView.as_view(), name='lista_empleados'),
    path('total-empleados/', TotalEmpleadosAPIView.as_view(), name='total_empleados'),
    path('add-empleado/', AddEmpleadoAPIView.as_view(), name='add_empleado'),
]