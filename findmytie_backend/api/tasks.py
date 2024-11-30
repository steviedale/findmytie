from celery import shared_task
import time
from .models import SearchQuery

# simulate loading in listings
time.sleep(10)

@shared_task
def process_search_query(search_query_id):
    print(f"Processing search query with id: {search_query_id}")
    search_query = SearchQuery.objects.get(id=search_query_id)
    print(f"Search query: {search_query}")
    # time.sleep(5)  # Simulate a long-running task
    # TODO: add logic for pairing search query with listings