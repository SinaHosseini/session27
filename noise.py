import cv2
import numpy as np

image_tv = cv2.imread("media/old_TV.jpg")
image_tv = cv2.cvtColor(image_tv, cv2.COLOR_BGR2GRAY)
row, cell = image_tv.shape

_, TV_image_thresh = cv2.threshold(image_tv, 250, 255, cv2.THRESH_BINARY)

writer = cv2.VideoWriter("media/TV_noise.mp4",
                         cv2.VideoWriter_fourcc(*'mp4v'), 40, (cell, row))

while True:
    noise = np.random.random((230, 300)) * 255
    noise = np.array(noise, dtype=np.uint8)
    noise_tv = noise*TV_image_thresh[40:270, 70:370] + image_tv[40:270, 70:370]
    frame = image_tv
    frame[40:270, 70:370] = noise_tv
    writer.write(frame)
    cv2.imshow("noise TV", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

writer.release()
