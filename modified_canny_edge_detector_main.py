import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from image_segmentation import image_segmentation
from get_color_channels import get_normalized_colors
from mced import mced
from get_center import get_center
from get_average_radius import get_average_radius

path = './orange.jpg'
img = Image.open(path)
img = img.resize((251, 251))
grayscale_image = ImageOps.grayscale(img)
red, green, blue = get_normalized_colors(np.array(img))
segmented_image = image_segmentation(grayscale_image)
res = mced(np.array(segmented_image), 1.5, (10, 10))
(x_center, y_center) = get_center(res)
average_radius = get_average_radius(res, x_center, y_center)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res, cmap='gray')
plt.tight_layout()
plt.show()
