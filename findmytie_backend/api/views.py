from django.shortcuts import render
from rest_framework import generics
from .models import SearchQuery, Listing
from .serializer import SearchQuerySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .tasks import process_search_query


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

        print(search_query)

        # TODO: kick off a celery task to process the search query
        # process_search_query.delay(search_query.id)
        print('starting celery task')
        ret = process_search_query.delay(search_query.id)
        print(f"celery task id: {ret.id}")

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

        # this is just dummy logic for now
        i = max(0, min(int(search_query_id), len(listings)) - 1)

        data = [{
            'id': listings[i].id,
            'title': listings[i].title,
            'price': listings[i].price,
            'url': listings[i].url,
            'image_url': listings[i].image.url,
            'created_at': listings[i].created_at,
        }]
        return Response(data, status=status.HTTP_200_OK)