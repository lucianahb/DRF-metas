from django.urls import include, path
from rest_framework import routers
from .views import SectorViewSet, CiaViewSet, TypeViewSet, GoalViewSet


router = routers.DefaultRouter()
router.register(r'sectors', SectorViewSet, basename="sectors")
router.register(r'cias', CiaViewSet, basename="cias")
router.register(r'types', TypeViewSet, basename="types")
router.register(r'goals', GoalViewSet, basename="goals")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
