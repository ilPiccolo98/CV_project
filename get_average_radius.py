import numpy as np
import math

def get_average_radius(image: np.ndarray, x_center: int, y_center: int):
    coordinates = np.argwhere(image == 255)
    average_radius = 0
    for coordinate in coordinates:
        average_radius += math.sqrt((coordinate[0] - x_center)**2 + (coordinate[1] - y_center)**2)
    average_radius /= coordinates.shape[0]
    return average_radius

