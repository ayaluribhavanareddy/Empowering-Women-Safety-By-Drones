import cv2
import numpy as np

# Start capturing video from the laptop's camera
cap = cv2.VideoCapture(0)


# Initialize variables for motion detection
prev_gray = None
threshold = 10000  # Adjust this threshold based on your environment

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_gray is not None:
        # Calculate the absolute difference between the current frame and the previous frame
        frame_diff = cv2.absdiff(prev_gray, gray)

        # Apply thresholding to get a binary image
        _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

        # Find contours in the binary image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Get the bounding rectangle of each contour
            x, y, w, h = cv2.boundingRect(contour)

            # Check if the contour area exceeds a threshold (large movement)
            if cv2.contourArea(contour) > threshold:
                # Draw a rectangle around the contour
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, 'Unwanted situation detected!', (40, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                break  # Exit the loop if a large movement is detected

    # Store the current frame for the next iteration
    prev_gray = gray

    # Display the frame
    cv2.imshow('Camera', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
