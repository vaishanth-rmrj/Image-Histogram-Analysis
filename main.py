import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img_color = cv2.imread("assets/images/0000000000.png", 0)

    plt.subplot(1, 1, 1), plt.imshow(img_color, cmap='gray') 
    plt.show()