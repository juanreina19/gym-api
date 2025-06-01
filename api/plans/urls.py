# from django.urls import path
from rest_framework import routers
from plans import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'plans', views.PlanViewSet, 'plans')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    
]