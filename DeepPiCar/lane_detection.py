import cv2
import numpy as np

def detect_lanes(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using Canny Edge Detection
    edges = cv2.Canny(blur, 50, 150)

    return edges

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Process frame to detect lanes
    lane_edges = detect_lanes(frame)

    # Show the detected lanes
    cv2.imshow("Lane Detection", lane_edges)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()