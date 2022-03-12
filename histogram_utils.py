import cv2
import numpy as np
import matplotlib.pyplot as plt

    
def fetch_histogram(gray_image):
    """
    function to get histogram plot

    Args:
        gray_image (numpy array)

    Returns:
        (hist_graph_x, hist_graph_y): x and y scale for the histogram graph
    """

    hist_intensities = [0 for _ in range(256)]

    for x in range(gray_image.shape[0]):
        for y in range(gray_image.shape[1]):
            hist_intensities[gray_image[x, y]] += 1   

    return [intensity_values for intensity_values in range(256)], hist_intensities      
