from rest_framework import serializers

from .models import Place

class SearchFirstLetters(serializers.ModelSerializer):
    model = Place
    fields = ('id', 'name')