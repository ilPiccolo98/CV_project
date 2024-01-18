from sobel_edge_detection import sobel_edge_detection
from non_max_suppression import non_max_suppression
from threshold_hysteresis import threshold_hysteresis
import numpy as np
from gaussian_blur import gaussianBlur
from to_gray import togray


def mced(image: np.ndarray, sigma: int | float, filter_shape, lowthreshold: float | int = 0.05, highthreshold: float | int = 0.09):
    blurred = gaussianBlur(image, sigma, filter_shape=filter_shape)[1] / 255
    squeezed_blurred = np.squeeze(blurred)
    padded = np.pad(squeezed_blurred, pad_width=1)
    G, theta = sobel_edge_detection(padded, "absolute")
    img = non_max_suppression(G, theta)
    img = threshold_hysteresis(img, lowthreshold, highthreshold * 1.562)
    return img