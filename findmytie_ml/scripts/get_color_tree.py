import pandas as pd
from sklearn.neighbors import KDTree
import numpy as np


def get_color_tree(df: pd.DataFrame, leaf_size=None, query_weight=[2, 10, 10]):
    # df['colors'] = [{'lab': [0, 0, 0], 'rgb': [0, 0, 0], 'weight': 0}]
    leaf_size = int(len(df) * 0.01) if leaf_size is None else leaf_size
    query_weight = np.array(query_weight)
    listing_ids = []
    listing_color_indices = []
    color_data = []
    color_pcts = []
    for _, row in df.iterrows():
        color_dicts = eval(row['colors'])
        for i, color_dict in enumerate(color_dicts):
            listing_ids.append(row['id'])
            lab = np.array(color_dict['lab'])
            color_data.append(lab * query_weight)
            color_pcts.append(color_dict['weight'])
            listing_color_indices.append(i)
    color_data = np.array(color_data)
    listing_ids = np.array(listing_ids)
    listing_color_indices = np.array(listing_color_indices)
    tree = KDTree(color_data, leaf_size=leaf_size, metric='euclidean')
    return {
        'tree': tree, 
        'listing_ids': listing_ids, 
        'listing_color_indices': listing_color_indices,
        'color_pcts': color_pcts, 
        'query_weight': query_weight,
    }