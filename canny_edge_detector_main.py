import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from ced import ced


path = './orange.jpg'
img = np.array(Image.open(path))
res = ced(img, 'rgb')
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res, cmap='gray')
plt.tight_layout()
plt.show()
