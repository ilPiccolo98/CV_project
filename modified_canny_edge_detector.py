import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from to_gray import togray
from image_segmentation import image_segmentation


path = './apple.jpg'
img = Image.open(path)
grayscale_image = ImageOps.grayscale(img)
segmented_image = image_segmentation(grayscale_image)
img = np.array(segmented_image.resize((251, 251)))
plt.imshow(img, cmap="gray")
plt.show()
