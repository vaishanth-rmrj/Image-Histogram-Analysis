import cv2
import numpy as np
import matplotlib.pyplot as plt

from histogram_utils import *

if __name__ == "__main__":
    img_gray = cv2.imread("assets/images/0000000000.png", 0)

    hist_graph_x, hist_graph_y = fetch_histogram(img_gray)

    plt.subplot(2, 1, 1), plt.imshow(img_gray, cmap='gray') 

    plt.subplot(2, 1, 2), plt.bar(hist_graph_x, hist_graph_y) 
    plt.subplot(2, 1, 2), plt.title("Histogram") 
    plt.subplot(2, 1, 2), plt.xlim((0, 260))
    plt.subplot(2, 1, 2), plt.xlabel("Intensity Range")
    plt.subplot(2, 1, 2), plt.ylabel("Intensity Count")
    plt.show()