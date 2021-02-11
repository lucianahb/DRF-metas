from rest_framework import serializers
from .models import Sector, Cia, Type_goal, Goal


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class CiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cia
        fields = '__all__'


class TypeGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_goal
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
