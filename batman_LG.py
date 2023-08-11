import cv2

image = cv2.imread("media/bat.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

row, cell = image.shape

_, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.putText(image, "BATMAN", (367, 500), cv2.FONT_HERSHEY_COMPLEX, 2, 255)

cv2.imwrite("media/output.jpg", image)
cv2.imshow("result", image)
cv2.waitKey()
