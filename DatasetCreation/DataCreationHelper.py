#Helper file

import cv2
import numpy as np
from matplotlib.patches import Polygon

def get_original_mask(image_size, annotations):
    height, width = image_size

    # create a single channel height, width pixel black image
    blank_image = np.zeros((height, width))

    # Create list of polygons to be drawn
    polygons_list = []

    # Add the polygon segmentation
    for segmentation_points in annotations["segmentation"]:
        segmentation_points = np.array(segmentation_points).reshape((int(len(segmentation_points)/2), 2))
        polygons_list.append(Polygon(segmentation_points))

    for poly in polygons_list:
        contours = poly.get_xy().astype(np.int32)
        cv2.fillPoly(blank_image, pts=[contours], color=(1, 1, 1))

    return blank_image
  
