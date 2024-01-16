import numpy as np

def get_color_channels(image: np.ndarray):
    red, green, blu = image[..., 0], image[..., 1], image[..., 2]
    return red, green, blu

def get_normalized_colors(image: np.ndarray):
    red, green, blue = get_color_channels(image)
    red_mean = np.mean(red)
    green_mean = np.mean(green)
    blue_mean = np.mean(blue)
    normalized_red = red_mean / (red_mean + green_mean + blue_mean)
    normalized_green = green_mean / (red_mean + green_mean + blue_mean)
    normalized_blue = blue_mean / (red_mean + green_mean + blue_mean)
    return normalized_red, normalized_green, normalized_blue
