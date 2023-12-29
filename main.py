import numpy as np
import cv2
import matplotlib.pyplot as plt

    
def sobelEdgeDetection(image: np.ndarray):
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
    Ix = cv2.filter2D(image, -1, Kx)
    Iy = cv2.filter2D(image, -1, Ky)
    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)
    return np.squeeze(G), np.squeeze(theta)


def non_max_suppression(img, theta):
    M, N = img.shape
    Z = np.zeros((M, N), dtype=np.int32)
    angle = theta * 180. / np.pi  
    angle[angle < 0] += 180      
    for i in range(1, M-1):
        for j in range(1, N-1):
            q = 255
            r = 255
            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                r = img[i, j-1]
                q = img[i, j+1]
            elif (22.5 <= angle[i, j] < 67.5):
                r = img[i-1, j+1]
                q = img[i+1, j-1]
            elif (67.5 <= angle[i, j] < 112.5):
                r = img[i-1, j]
                q = img[i+1, j]
            elif (112.5 <= angle[i, j] < 157.5):
                r = img[i+1, j+1]
                q = img[i-1, j-1]
            if (img[i, j] >= q) and (img[i, j] >= r):
                Z[i, j] = img[i, j]
            else:
                Z[i, j] = 0
    return Z


def threshold_hysteresis(img: np.ndarray, lowThresholdRatio=0.05, highThresholdRatio=0.09, weak=np.int32(25)):
    highThreshold = img.max() * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio
    M, N = img.shape
    res = np.zeros((M, N), dtype=np.int32)
    strong = np.int32(255)
    strong_i, strong_j = np.where(img >= highThreshold)
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (res[i, j] == weak):
                if (
                    (res[i+1, j-1] == strong) or (res[i+1, j] == strong) or
                    (res[i+1, j+1] == strong) or (res[i, j-1] == strong) or
                    (res[i, j+1] == strong) or (res[i-1, j-1] == strong) or
                    (res[i-1, j] == strong) or (res[i-1, j+1] == strong)
                ):
                    res[i, j] = strong
                else:
                    res[i, j] = 0
    return res



image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(image, (5,5), 0)
G, theta = sobelEdgeDetection(blurred)
image = non_max_suppression(G, theta)
image = threshold_hysteresis(G, theta)
plt.imshow(image)
plt.show()
