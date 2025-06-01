from .models import Plan
from .serializers import PlanSerializer
from rest_framework import viewsets, permissions

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.AllowAny]

    