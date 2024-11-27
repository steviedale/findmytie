from rest_framework import serializers
from .models import SearchQuery


class SearchQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchQuery
        fields = [
            'id', 'code', 'color_1', 'color_2', 'color_3', 'host', 
            'created_at'
        ]