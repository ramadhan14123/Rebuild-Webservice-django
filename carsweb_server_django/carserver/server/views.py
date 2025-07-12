from rest_framework import viewsets, filters
from .models import TBCarsWeb
from .serializers import TBCarsWebSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = TBCarsWeb.objects.all().order_by('-id')
    serializer_class = TBCarsWebSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['carname', 'carbrand', 'carmodel'] 

