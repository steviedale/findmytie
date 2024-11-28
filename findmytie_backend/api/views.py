from django.shortcuts import render
from rest_framework import generics
from .models import SearchQuery
from .serializer import SearchQuerySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SearchQueryView(generics.ListAPIView):
    queryset = SearchQuery.objects.all()
    serializer_class = SearchQuerySerializer

class CreateSearchQueryView(APIView):
    serializer_class = SearchQuerySerializer

    def post(self, request, format=None):
        if not self.request.data:
            return Response({'Error': 'No data found'})

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            host = self.request.session.session_key
            colors = serializer.data.get('colors')
            search_query = SearchQuery.objects.create(host=host, colors=colors)
            return Response(SearchQuerySerializer(search_query).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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