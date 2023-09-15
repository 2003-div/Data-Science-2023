import cv2
import numpy as np

# Create a video capture object
WEBCAM_IDX = 0 
cam = cv2.VideoCapture(WEBCAM_IDX)
cv2.namedWindow('image')  # image
cv2.createTrackbar('min','image',0,255,lambda x:x)
cv2.createTrackbar('max','image',0,1000,lambda x:x)
cv2.createTrackbar('xpos','image',0,640,lambda x:x)
cv2.createTrackbar('ypos','image',0,480,lambda x:x)

while cam.isOpened():
    # Capture image from Camera
    state , image = cam.read()
    if not state:break # if state is none then break loop

    # get trackbar values
    minval = cv2.getTrackbarPos('min','image')
    maxval = cv2.getTrackbarPos('max','image')
    filter = cv2.Canny(image,minval,maxval)
    xp = cv2.getTrackbarPos('xpos','iamge')
    yp = cv2.getTrackbarPos('ypos','image')
    image = cv2.putText(image,"Computer vision",(xp,yp),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))
    # show image
    cv2.imshow('filter',filter)
    cv2.imshow('image',image)
    # wait for a key press
    key = cv2.waitKey(10)
    # if esc key is pressed exit loop
    if key == 27:
        break

# release camera
cam.release()
cv2.destroyAllWindows()