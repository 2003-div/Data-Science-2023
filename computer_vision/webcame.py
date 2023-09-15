import cv2
import numpy as np

# Create a video capture object
WEBCAM_IDX = 0 
cam = cv2.VideoCapture(WEBCAM_IDX)
while cam.isOpened():
    # Capture image from Camera
    state , image = cam.read()
    if not state:break # if state is none then break loop
    # show image
    cv2.imshow('image',image)
    # wait for a key press
    key = cv2.waitKey(10)
    # if esc key is pressed exit loop
    if key == 27:
        break

# release camera
cam.release()
cv2.destroyAllWindows()