import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from image_segmentation import image_segmentation
from get_color_channels import get_normalized_colors
from mced import mced

path = './orange.jpg'
img = np.array(Image.open(path))
res = mced(img, 1.5, (10, 10), 'rgb')
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res, cmap='gray')
plt.tight_layout()
plt.show()

'''
path = './orange.jpg'
img = Image.open(path)
red, green, blue = get_normalized_colors(np.array(img))
print(red, green, blue)
grayscale_image = ImageOps.grayscale(img)
segmented_image = image_segmentation(grayscale_image)
img = np.array(segmented_image.resize((251, 251)))
plt.imshow(img, cmap="gray")
plt.show()
'''


