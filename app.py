import cv2
import numpy as np

cap = cv2.VideoCapture(0)


prev_gray = None
threshold = 10000  

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_gray is not None:
        frame_diff = cv2.absdiff(prev_gray, gray)

        _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)

            if cv2.contourArea(contour) > threshold:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, 'Unwanted situation detected!', (40, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                break  # Exit the loop if a large movement is detected

    prev_gray = gray

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
