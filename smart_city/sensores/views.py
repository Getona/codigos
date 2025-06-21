from rest_framework import viewsets, filters
from .models import Sensor, Ambiente, Historico
from .serializers import SensorSerializer, AmbienteSerializer, HistoricoSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['sensor', 'unidade_med', 'status']
    ordering_fields = ['sensor']

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['sig', 'descricao', 'ni']

class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['sensor__sensor', 'timestamp', 'ambiente__sig']
