import cv2

# Open the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read a frame from the webcam

    if not ret:
        print("Failed to capture image")
        break

    cv2.imshow("Camera Feed", frame)  # Show the frame in a window

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close the window