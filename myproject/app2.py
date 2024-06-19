import cv2 as cv
import numpy as np
import boto3
from termcolor import colored
from pyvirtualdisplay import Display



# Initialize AWS Rekognition client
rekognition_client = boto3.client('rekognition', region_name='ap-south-1')



# Load Haarcascades for face and eye detection
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')



# Function to detect face and eyes using AWS Rekognition and Haarcascades
def detect_face_and_eyes(frame, rekognition_client):
  
  
    # Convert the OpenCV frame to bytes
    _, img_encoded = cv.imencode('.jpg', frame)
    img_bytes = img_encoded.tobytes()



    # Your code for AWS Rekognition...
    response = rekognition_client.detect_faces(
        Image={'Bytes': img_bytes},
        Attributes=['ALL']
    )



    # Extract information from the AWS Rekognition response
    for face in response['FaceDetails']:
        # Draw a rectangle around the detected face in blue
        bbox = face['BoundingBox']
        image_height, image_width, _ = frame.shape
        x, y, w, h = int(bbox['Left'] * image_width), int(bbox['Top'] * image_height), \
                     int(bbox['Width'] * image_width), int(bbox['Height'] * image_height)

        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle for face




        # Detect eyes using Haarcascades in the region of the detected face
        roi_gray = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Draw rectangles around detected eyes in red
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 0, 255), 2)  # Red rectangle for eyes



        # Display the confidence score on the image
        confidence = face['Confidence']
        cv.putText(frame, f"Confidence: {confidence:.2f}", (x, y - 10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # Blue text for confidence



        # Print the confidence for each face
        print(f"Confidence for Face: {confidence:.2f}")



# Use virtual display
with Display():
    # Read a static image
    frame = cv.imread('elon.jpg')

    # Convert the frame to grayscale for face detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces using the Haarcascade classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate through detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle for face

        # Draw a circle at the center of the detected face
        cv.circle(frame, (x + int(w * 0.5), y + int(h * 0.5)), 4, (255, 0, 0), -1)  # Blue circle for face center

        # Detect eyes for the current face
        detect_face_and_eyes(frame, rekognition_client)

    # Save the result as an image (optional)
    cv.imwrite('result_with_eyes.jpg', frame)

    # Print a message to indicate the script has finished
    print("Face and eye detection completed. Results saved to 'result_with_eyes.jpg'.")
