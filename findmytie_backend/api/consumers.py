# consumers.py
import json
import time

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import SearchQuery, Listing, QueryMatch


class GetListingsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    @database_sync_to_async
    def get_search_queries(self, search_query_id):
        search_queries = list(SearchQuery.objects.filter(id=search_query_id))
        return search_queries

    @database_sync_to_async
    def get_listings(self, search_query):
        listing_ids = list(QueryMatch.objects.filter(search_query=search_query).values_list('listing', flat=True))
        listings = list(Listing.objects.filter(id__in=listing_ids))
        print(f"TYPE listings: {type(listings)}")
        return listings

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(f"GetListingsConsumer received data: {data}")
        if 'search_query_id' not in data:
            await self.send(text_data=json.dumps({'error': 'No search_query_id found in data'}))
            return
        search_query_id = data['search_query_id']
        search_query = await self.get_search_queries(search_query_id)

        if len(search_query) == 0:
            await self.send(text_data=json.dumps({'error': 'SearchQuery not found'}))
            return
        if len(search_query) > 1:
            await self.send(text_data=json.dumps({'error': 'Multiple SearchQuery found'}))
            return
        
        search_query = search_query[0]

        if search_query.completed:
            listings = await self.get_listings(search_query)
            print(type(listings))
            print(listings)
            json_obj = {'listings': [
                {
                    'listing_id': listing.id,
                    'title': listing.title, 
                    'price': str(listing.price), 
                    'url': listing.url, 
                    'image_url': listing.image.url,
                    'created_at': str(listing.created_at),
                } for listing in listings
            ]}
            await self.send(text_data=json.dumps(json_obj))
        else:
            await self.send(text_data=json.dumps({'message': 'Not complete yet'}))


