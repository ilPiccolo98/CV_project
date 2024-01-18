from sobel_edge_detection import sobel_edge_detection
from non_max_suppression import non_max_suppression
from threshold_hysteresis import threshold_hysteresis
import numpy as np
from to_gray import togray


def ced(image: np.ndarray, lowthreshold: float | int = 0.05, highthreshold: float | int = 0.09):
    G, theta = sobel_edge_detection(image, "euclidean")
    img = non_max_suppression(G, theta)
    img = threshold_hysteresis(img, lowthreshold, highthreshold)
    return img