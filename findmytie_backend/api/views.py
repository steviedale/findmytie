from django.shortcuts import render
from rest_framework import generics
from .models import SearchQuery, Listing
from .serializer import SearchQuerySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


class ListSearchQueryView(generics.ListAPIView):
    queryset = SearchQuery.objects.all()
    serializer_class = SearchQuerySerializer

class CreateSearchQueryView(APIView):
    serializer_class = SearchQuerySerializer

    def post(self, request, format=None):
        if not self.request.data:
            return Response({'Error': 'No data found'})

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        data = request.data

        host = self.request.session.session_key
        search_query = SearchQuery.objects.create(host=host, colors=str(data['colors']))

        return Response(SearchQuerySerializer(search_query).data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetSearchQueryView(APIView):
    serializer_class = SearchQuerySerializer

    def get(self, request, format=None):
        host = request.GET.get('host')

        if not host:
            return Response({'Error': 'No data found'}, status=status.HTTP_400_BAD_REQUEST)

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        # host = self.request.session.session_key
        search_query = SearchQuery.objects.filter(host=host)
        print('host: ', host)
        print('sending data: ', search_query)
        return Response(SearchQuerySerializer(search_query, many=True).data, status=status.HTTP_200_OK)

class GetListingsView(APIView):

    def get(self, request, format=None):
        search_query_id = request.GET.get('search-query-id')
        print('search_query_id: ', search_query_id)
        search_query = SearchQuery.objects.filter(id=search_query_id)
        print('search_query: ', search_query)
        if len(search_query) > 0:
            # colors = json.loads(search_query[0].colors)
            colors = search_query[0].colors
            print(f"colors: {colors}")

        listings = Listing.objects.all()
        print(f"listings: {listings}")

        data = [{
            'id': listings[0].id,
            'title': listings[0].title,
            'price': listings[0].price,
            'url': listings[0].url,
            'image_url': listings[0].image.url,
            'created_at': listings[0].created_at,
        }]
        return Response(data, status=status.HTTP_200_OK)