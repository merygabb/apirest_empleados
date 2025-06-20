from .serializers import EmpleadoSerializer
from rest_framework import generics
from .models import Empleado
from rest_framework.response import Response
from rest_framework import status

class EmpleadoListAPIView(generics.ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class TotalEmpleadosAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        total_empleados = Empleado.objects.count()
        return Response({'total_empleados': total_empleados}, status=status.HTTP_200_OK)
    
class AddEmpleadoAPIView(generics.CreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)