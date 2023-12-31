import cv2

cap = cv2.VideoCapture(0)

_, frame = cap.read()

rows = frame.shape[0]
cols = frame.shape[1]

writer = cv2.VideoWriter(
    "media/result.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (rows, cols))

while True:
    _, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    writer.write(frame)
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

writer.release()
