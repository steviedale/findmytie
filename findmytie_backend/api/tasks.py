from celery import shared_task
import time
from .models import SearchQuery, Listing, QueryMatch
import sys
import pandas as pd
import numpy as np
import cv2

sys.path.append('../findmytie_ml')
from scripts.get_color_tree import get_color_tree


print('Loading data...')
df = pd.read_csv('/Users/sdale/repos/findmytie/findmytie_backend/api/data/manual_listings_with_colors.csv')
tree_data = get_color_tree(df)
listing_tree = tree_data['tree'] 
listing_ids = tree_data['listing_ids']
listing_color_indices = tree_data['listing_color_indices']
color_pcts = tree_data['color_pcts']
query_weight = tree_data['query_weight']
print('Data loaded.')

# simulate loading in listings
# time.sleep(10)

# TODO: test this
@shared_task
def process_search_query(search_query_id):
    print(f"Processing search query with id: {search_query_id}")
    search_query = SearchQuery.objects.get(id=search_query_id)
    print(f"Search query: {search_query}")

    colors_str = search_query.colors
    colors = eval(colors_str)
    rgb_colors = [tuple(int(c[i:i+2], 16) for i in (1, 3, 5)) for c in colors]
    # rgb_colors = np.array([rgb_colors], np.float32)
    rgb_colors = np.array([rgb_colors], np.uint8)
    lab_colors = cv2.cvtColor(rgb_colors, cv2.COLOR_RGB2LAB)
    query_colors = lab_colors
    # print(lab_colors)
    # print(rgb_colors)

    # TODO: do this for more than just the first color
    query_color_index = 0
    query_color = query_colors[query_color_index]
    distances, indices = listing_tree.query([query_color * query_weight], k=5)

    for ind, dist in zip(indices, distances):
        print(f"Distance: {dist}")
        print(f"Index: {ind}")

        listing_id = listing_ids[ind]
        listing = Listing.objects.get(id=listing_id)

        assert(len(df[df['id'] == listing_id]) == 1)
        listing_colors = eval(df[df['id'] == listing_id].iloc[0]['colors'])
        listing_color = listing_colors[listing_color_indices[ind]['lab']]

        query_match = QueryMatch(
            search_query=search_query, 
            listing_id=listing, 

            query_color_index=query_color_index,
            listing_color_index=listing_color_indices[ind],

            distance=dist, 
            query_color=query_color, 
            listing_color=listing_color,
        )
        query_match.save()
    
    search_query.completed = True
    search_query.save()