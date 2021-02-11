from rest_framework import viewsets
from .serializers import SectorSerializer, CiaSerializer, \
    TypeGoalSerializer, GoalSerializer
from .models import Cia, Goal, Sector, Type_goal


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all().order_by('id')
    serializer_class = SectorSerializer


class CiaViewSet(viewsets.ModelViewSet):
    queryset = Cia.objects.all().order_by('id')
    serializer_class = CiaSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type_goal.objects.all().order_by('id')
    serializer_class = TypeGoalSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all().order_by('end_date')
    serializer_class = GoalSerializer
