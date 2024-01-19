import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from image_segmentation import image_segmentation
from get_color_channels import get_normalized_colors
from mced import mced
from get_center import get_center
from get_average_radius import get_average_radius
from os import listdir
from os.path import isfile, join
from fruit_recognition import fruit_recognition
from fruit_classification import fruit_classification

#training phase
print("TRAINING PHASE-----------------")
path = "./dataset/Oranges"
files = [f for f in listdir(path) if isfile(join(path, f))]
red_intensities = []
green_intensities = []
diff_intensities = []
average_radiuses = []
for filename in files:
    img = Image.open(path + "/" + filename)
    img = img.resize((251, 251))
    grayscale_image = ImageOps.grayscale(img)
    red, green, blue = get_normalized_colors(np.array(img))
    red_intensities.append(red)
    green_intensities.append(green)
    diff_intensities.append(red - green)
    segmented_image = image_segmentation(grayscale_image)
    res = mced(np.array(segmented_image), 1.5, (10, 10))
    (x_center, y_center) = get_center(res)
    average_radius = get_average_radius(res, x_center, y_center)
    average_radiuses.append(average_radius)

th_lower_radius = min(average_radiuses) - 5
th_upper_radius = max(average_radiuses) + 5
th_upper_intensity_diff = max(diff_intensities)
th_lower_intensity_diff = min(diff_intensities)
th_orange_radius = np.mean(average_radiuses)
th_orange_red_intensity = np.mean(red) - 0.07
print("th_orange_radius: ", th_orange_radius)
print("th_orange_red_intensity: ", th_orange_red_intensity)

path = "./dataset/Apples/green"
files = [f for f in listdir(path) if isfile(join(path, f))]
red_intensities = []
green_intensities = []
diff_intensities = []
average_radiuses = []
for filename in files:
    img = Image.open(path + "/" + filename)
    img = img.resize((251, 251))
    grayscale_image = ImageOps.grayscale(img)
    red, green, blue = get_normalized_colors(np.array(img))
    red_intensities.append(red)
    green_intensities.append(green)
    diff_intensities.append(red - green)
    segmented_image = image_segmentation(grayscale_image)
    res = mced(np.array(segmented_image), 1.5, (10, 10))
    (x_center, y_center) = get_center(res)
    average_radius = get_average_radius(res, x_center, y_center)
    average_radiuses.append(average_radius)

th_green_intensity = min(green_intensities)

path = "./dataset/Apples/red"
files = [f for f in listdir(path) if isfile(join(path, f))]
red_intensities = []
green_intensities = []
diff_intensities = []
for filename in files:
    img = Image.open(path + "/" + filename)
    img = img.resize((251, 251))
    grayscale_image = ImageOps.grayscale(img)
    red, green, blue = get_normalized_colors(np.array(img))
    red_intensities.append(red)
    green_intensities.append(green)
    diff_intensities.append(red - green)
    segmented_image = image_segmentation(grayscale_image)
    res = mced(np.array(segmented_image))
    (x_center, y_center) = get_center(res)
    average_radius = get_average_radius(res, x_center, y_center)
    average_radiuses.append(average_radius)

th_apple_radius = np.mean(average_radiuses)
print("th_apple_radius: ", th_apple_radius)

'''
print("th_lower_radius: ", th_lower_radius)
print("th_upper_radius: ", th_upper_radius)
print("th_upper_intensity_diff", th_upper_intensity_diff)
print("th_lower_intensity_diff", th_lower_intensity_diff)
print("th_green_intensity", th_green_intensity)
'''

path = ""
while path != "exit":
    path = input("Insert path: ")
    if path != "exit":
        img = Image.open(path)
        img = img.resize((251, 251))
        grayscale_image = ImageOps.grayscale(img)
        red, green, blue = get_normalized_colors(np.array(img))
        segmented_image = image_segmentation(grayscale_image)
        res = mced(np.array(segmented_image), 1.5, (10, 10))
        (x_center, y_center) = get_center(res)
        average_radius = get_average_radius(res, x_center, y_center)
        detection = fruit_recognition(green, red, average_radius, th_green_intensity, th_lower_radius, th_upper_radius, th_lower_intensity_diff, th_upper_intensity_diff)
        print(detection)
        classification = fruit_classification(detection, red, green, average_radius, th_apple_radius, th_orange_radius, th_orange_red_intensity)
        print(classification)


