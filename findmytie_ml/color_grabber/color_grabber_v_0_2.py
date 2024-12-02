# %%
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# %%
import sys
sys.path.append('..')
from semantic_segmentation.semantic_segmentation_v_0 import get_segmentation_mask

# %%
SIZE = 256

def grab_colors(
    img,  # opencv image
    n_colors=8, 
    weights=(5, 100, 100, 1, 1), 
    resize=False,
    resize_to=SIZE,
    blur=True, 
    remove_background=True, 
    output_format='rgb',
    remove_dark_points=True,
    dark_pct_thresh=5,
    remove_grey_points=True,
    grey_pct_thresh=20,
    max_grey_thresh=10,
    seed=42,
    verbose=False,
):
    # TODO: consider returning a mask of the points used to calculate the colors

    if resize:
        img = cv2.resize(img, (resize_to, resize_to))

    # remove background (part 1 of 2)
    if remove_background:
        foreground_mask = get_segmentation_mask(img)
        foreground_mask = foreground_mask.reshape(-1)
        foreground_mask = foreground_mask.astype(bool)

    if blur:
        img = cv2.GaussianBlur(img, (5, 5), 3)

    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    clt = KMeans(n_clusters=n_colors, random_state=seed)

    # Get positional row/col channels to append to the points
    row_channel = np.arange(img_lab.shape[0]).reshape(-1, 1) / img_lab.shape[0]
    row_channel = np.repeat(row_channel, img_lab.shape[1], axis=1)
    col_channel = np.arange(img_lab.shape[1]).reshape(1, -1) / img_lab.shape[1]
    col_channel = np.repeat(col_channel, img_lab.shape[0], axis=0)
    img_lab = np.dstack((img_lab, row_channel, col_channel))

    points = img_lab.reshape(-1, 5)

    # remove background (part 2 of 2)
    if remove_background:
        n1 = points.shape[0]
        points = points[foreground_mask]
        n2 = points.shape[0]
        if verbose:
            print(f"Removed {n1 - n2} background points")

    # remove % darkest points
    if remove_dark_points:
        n1 = points.shape[0]
        th = np.percentile(points[:, 0], dark_pct_thresh)
        points = points[points[:, 0] >= th]
        n2 = points.shape[0]
        assert(n2 > 0)
        if verbose:
            print(f"Removing points with L < {th}")
            print(f"Removed {n1 - n2} dark points")
    
    # remove 20% grey-est points
    if remove_grey_points:
        a = points[:, 1] - 128
        b = points[:, 2] - 128
        ab_sum = np.abs(a) + np.abs(b)
        th = np.percentile(ab_sum, grey_pct_thresh)
        th = min(th, max_grey_thresh)
        grey_mask = ab_sum < th
        n1 = points.shape[0]
        points = points[~grey_mask]
        n2 = points.shape[0]
        if verbose:
            print(f"Removing points with a+b < {th}")
            print(f"Removed {n1 - n2} grey points")

    points = points * np.array(weights)
    labels = clt.fit_predict(points)
    cluster_weights = np.bincount(labels)
    cluster_weights = cluster_weights / cluster_weights.sum()
    closest_points = []
    centroids = clt.cluster_centers_
    for centroid in centroids:
        lab_centroid = centroid[:3]
        closest_point = points[np.argmin(np.linalg.norm(points[:, :3] - lab_centroid, axis=1))]
        closest_points.append(closest_point)
    closest_points = np.array(closest_points)
    closest_points = closest_points / np.array(weights)
    centroids = centroids / np.array(weights)
    inertia = clt.inertia_

    centroids = centroids[:, :3]
    closest_points = closest_points[:, :3]

    # convert output color
    if output_format == 'rgb':
        centroids = cv2.cvtColor(centroids.astype(np.uint8).reshape(1, -1, 3), cv2.COLOR_LAB2RGB).reshape(-1, 3)
        closest_points = cv2.cvtColor(closest_points.astype(np.uint8).reshape(1, -1, 3), cv2.COLOR_LAB2RGB).reshape(-1, 3)
    else:
        assert(output_format == 'lab')
    
    return centroids, cluster_weights, closest_points, inertia
