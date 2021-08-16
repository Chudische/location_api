from rest_framework import serializers

from .models import Place


class PlaceIdName(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name')


class PlaceFullName(serializers.ModelSerializer):
    name = serializers.CharField(source='__str__')
    full_name = serializers.CharField(source='all_parents_name')

    class Meta:
        model = Place
        fields = ('id', 'name', 'full_name')


class PlaceAllParents(serializers.ModelSerializer):
    all_parents_name = serializers.CharField()
    name = serializers.CharField(source='__str__')

    class Meta:
        model = Place
        fields = ('id', 'name', 'all_parents_name')