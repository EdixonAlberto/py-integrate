from rest_framework import viewsets
from app.models import Equations
from app.serializer import EquationsSerializer

class EquationsViewSet(viewsets.ModelViewSet):
    queryset = Equations.objects.all()
    serializer_class = EquationsSerializer
