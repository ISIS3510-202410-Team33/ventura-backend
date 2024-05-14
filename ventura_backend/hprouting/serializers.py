from rest_framework import serializers
from .models import *


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class SiteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteType
        fields = '__all__'


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class SiteAdjacencySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteAdjacency
        fields = '__all__'
