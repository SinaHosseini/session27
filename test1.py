import cv2

image = cv2.imread("eye.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

row, cell = image.shape

threshold = 100

# image[image > threshold] = 255
# image[image <= threshold] = 0

_, image2 = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("result", image2)
cv2.waitKey()

