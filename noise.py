import cv2
import numpy as np

image_tv = cv2.imread("old_TV.jpg")
image_tv - cv2.cvtColor(image_tv, cv2.COLOR_BGR2GRAY)

row, cell = image_tv.shape
