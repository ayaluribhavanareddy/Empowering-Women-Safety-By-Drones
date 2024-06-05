import cv2
import numpy as np

# Load the trained model
model = tf.keras.models.load_model( r'C:\Users\megha\OneDrive\Desktop\Real Life Violence Dataset')

# Start capturing video from the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preprocess the frame
    resized_frame = cv2.resize(frame, (224, 224))
    normalized_frame = resized_frame / 255.0
    input_frame = np.expand_dims(normalized_frame, axis=0)
    
    # Perform inference
    prediction = model.predict(input_frame)
    
    # Display the inference result
    if prediction[0][0] > 0.5:
        cv2.putText(frame, 'Gesture detected!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
