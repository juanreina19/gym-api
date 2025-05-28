from django.urls import path
from .views import plans
from rest_framework import routers
from .api import PlanViewSet

router = routers.DefaultRouter()
router.register('api/plans', PlanViewSet, 'plans')

urlpatterns = router.urls