import numpy as np
from convolution import convolution


def sobel_edge_detection(image: np.ndarray, magnitude="euclidean"):
    Kx = np.array(
        [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]], np.float32
    )
    Ky = np.array(
        [[1, 2, 1],
         [0, 0, 0],
         [-1, -2, -1]], np.float32
    )
    Ix = convolution(image, Kx)
    Iy = convolution(image, Ky)
    G = None
    if magnitude == "euclidean":
        G = np.hypot(Ix, Iy)
    elif magnitude == "absolute":
        G = np.absolute(Ix) + np.absolute(Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)
    return np.squeeze(G), np.squeeze(theta)