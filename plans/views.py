from .models import Plan
from .serializers import PlanSerializer
from rest_framework import viewsets, permissions

from django.shortcuts import render, redirect

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.AllowAny]

def documentation(request):
    return render(request, 'doc.html')

def redirect_to_docs(request):
    return redirect('/docs/')