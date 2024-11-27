from django.shortcuts import render
from rest_framework import generics
from .models import SearchQuery
from .serializer import SearchQuerySerializer


# Create your views here.
class CreateSearchQueryView(generics.CreateAPIView):
    queryset = SearchQuery.objects.all()
    serializer_class = SearchQuerySerializer


class SearchQueryView(generics.ListAPIView):
    queryset = SearchQuery.objects.all()
    serializer_class = SearchQuerySerializer