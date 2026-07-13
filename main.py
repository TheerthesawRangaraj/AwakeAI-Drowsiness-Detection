import cv2
import os

# Get the folder where main.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build full path to the video
video_path = os.path.join(base_dir, "input.mp4")

print("Video path:", video_path)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Failed to open video.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Driver Drowsiness Demo", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()