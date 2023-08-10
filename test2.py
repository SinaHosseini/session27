import cv2
import numpy as np

my_image = np.zeros((450, 510), dtype=np.uint8)

# my_image = np.random.random((250, 350)) * 255
# my_image = np.array(my_image, dtype=np.uint8)

cv2.rectangle(my_image, (0, 0), (410, 350), 128, 10)
cv2.putText()

cv2.imshow("result", my_image)
cv2.waitKey()
