import numpy as np
import math


def get_center(image: np.ndarray):
    height, width = image.shape
    return (math.floor(width / 2), math.floor(height / 2))