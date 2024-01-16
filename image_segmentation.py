from PIL import Image

def image_segmentation(image: Image):
    image = image.convert("L")
    threshold = 210
    image_threshold = image.point(lambda x: 255 if x > threshold else 0)
    return image_threshold
