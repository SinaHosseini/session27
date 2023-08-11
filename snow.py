import cv2
import numpy as np

image = cv2.imread("media/snow_pic.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image, (430, 600), interpolation=cv2.INTER_LINEAR)

height, width = image.shape

writer = cv2.VideoWriter(
    "media/snow_vid.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 24, (width, height))

while True:
    frame = image.copy()

    num_snowflakes = np.random.randint(50, 150)

    snowflake_x = np.random.randint(0, width, num_snowflakes)
    snowflake_y = np.random.randint(0, height, num_snowflakes)

    for x, y in zip(snowflake_x, snowflake_y):
        cv2.circle(frame, (x, y), 2, (255, 255), -1)

    cv2.imshow("snow VID", frame)

    writer.write(frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

writer.release()
