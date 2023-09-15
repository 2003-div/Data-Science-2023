import cv2 
import numpy as np

# File path
file = r'C:\Users\sriva\Videos\Captures\Windows Screen Recorder Shortcut. - YouTube - Google Chrome 2023-06-25 18-01-56.mp4'
vid = cv2.VideoCapture(file)

while True:
    state , image = vid.read()
    if not state:break
    # resize to 500 by 500
    sm_image_1 = cv2.resize(image,(500,500))
    sm_image_2 = cv2.resize(image , None , fx = .25,fy = .25) # scaledowm by 25%
    # filter 
    bw_image = cv2.cvtColor(sm_image_2,cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(sm_image_2,cv2.COLOR_BGR2RGB)
    # edge filter for outlines
    edge_image = cv2.Canny(rgb_image,100,200)
    cv2.imshow('video 1',sm_image_1)
    cv2.imshow('video 2',sm_image_2)
    cv2.imshow('bw',bw_image)
    cv2.imshow('rgb',rgb_image)
    cv2.imshow('edge',edge_image)
    key = cv2.waitKey(10)
    if key ==27 :break
cv2.destroyAllWindows()
vid.release()