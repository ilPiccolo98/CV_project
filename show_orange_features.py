import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from image_segmentation import image_segmentation
from get_color_channels import get_normalized_colors
from mced import mced
from ced import ced
from get_center import get_center
from get_average_radius import get_average_radius
from os import listdir
from os.path import isfile, join
from fruit_recognition import fruit_recognition


path = "./test_set_2"
files = [f for f in listdir(path) if isfile(join(path, f))]
for filename in files:
    print("")
    print("File: ", filename, "--------------------")
    img = Image.open(path + "/" + filename)
    img = img.resize((251, 251))
    grayscale_image = ImageOps.grayscale(img)
    red, green, blue = get_normalized_colors(np.array(img))
    print("Red intensity: ", red)
    print("Green intensity: ", green)
    print("Red intensity - Green intensity: ", red - green)
    segmented_image = image_segmentation(grayscale_image)
    #res = mced(np.array(segmented_image), 1.5, (10, 10))
    res = ced(np.array(segmented_image))
    (x_center, y_center) = get_center(res)
    average_radius = get_average_radius(res, x_center, y_center)
    print("Average radius: ", average_radius)
    print(fruit_recognition(green, red, average_radius, 0.34123, 70, 90, 0, 0.11))
