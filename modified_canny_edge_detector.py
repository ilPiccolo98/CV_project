import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from image_segmentation import image_segmentation
from get_color_channels import get_normalized_colors


path = './orange.jpg'
img = Image.open(path)
red, green, blue = get_normalized_colors(np.array(img))
print(red, green, blue)
grayscale_image = ImageOps.grayscale(img)
segmented_image = image_segmentation(grayscale_image)
img = np.array(segmented_image.resize((251, 251)))
plt.imshow(img, cmap="gray")
plt.show()
