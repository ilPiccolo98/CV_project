import numpy as np
from convolution import convolution


def gaussianBlur(img: np.ndarray, sigma: float | int, filter_shape: list | tuple | None = None):
    if filter_shape == None:
        _ = 2 * int(4 * sigma + 0.5) + 1
        filter_shape = [_, _]
    gaussian_filter = np.zeros((filter_shape[0], filter_shape[1]), np.float32)
    size_y = filter_shape[0] // 2
    size_x = filter_shape[1] // 2
    x, y = np.mgrid[-size_y:size_y+1, -size_x:size_x+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    gaussian_filter = np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    filtered = convolution(img, gaussian_filter)
    return gaussian_filter, filtered.astype(np.uint8)