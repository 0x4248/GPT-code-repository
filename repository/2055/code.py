import cv2
import numpy as np

# Load the pre-trained face detection and face recognition models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the face recognition model on the faces of known individuals
images = []
labels = []

for i in range(1, 11):
    for j in range(1, 6):
        img = cv2.imread(f'faces/person{i}_{j}.jpg', cv2.IMREAD_GRAYSCALE)
        images.append(img)
        labels.append(i)

recognizer.train(images, np.array(labels))

# Open the video capture device
cap = cv2.VideoCapture(0)

# Loop over frames from the video stream
while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop over the detected faces
    for (x, y, w, h) in faces:
        # Extract the face region from the frame and resize it to the size expected by the face recognition model
        face_roi = gray[y:y+h, x:x+w]
        face_roi = cv2.resize(face_roi, (100, 100))

        # Recognize the face using the face recognition model
        label, confidence = recognizer.predict(face_roi)

        # Draw a rectangle around the detected face and display the label and confidence score
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"Person {label}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.putText(frame, f"Confidence: {int(confidence)}%", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
