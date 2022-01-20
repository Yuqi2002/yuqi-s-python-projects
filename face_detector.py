# face detector
import cv2
from random import randrange 

# loading pre-trained data from open cv
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam=cv2.VideoCapture(0)
 
# loops forever over frames until user ends video
while True: 
    #read the current frame
    successful_frame_read, frame=webcam.read()

    # converts image to black and white so it's easier for ai to recognize
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # detect faces
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

    # draws a rectangle around the faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),4)

    # shows the video live 
    cv2.imshow("Yuqi's Face Detector",frame)
    key=cv2.waitKey(1)

    # quits the program if space or q is pressed
    if key==32 or key==113:
        break 
    
# how does this algorithm work?
# haarcascade is an algorithm that is a chain of events that reads every 
# square of the image and uses machine learning to identify the faces in the image

# haarcascade uses edge features, line features and four-rectangle features
# to determine the right combination of pixle features that make a face 
# when it "reads" the image, it scans it from left to right to see if any 
# combination of light to dark or dark to light pixels added together matches
# the template of the face 
# this is why grayscale images are easier to detect since it's just light and dark
# you could use colored images to detect race or skin-color

# how is this data trained?
# it starts with supervised learning where we feed images to haarcascade in two 
# categories, positive image and negative image(faces and non-faces)

# supervised machine learning is where a human trains the machine by feeding it
# in this case, images and labeling them 

# unsupervised machine learning is where images are being fed to the machine 
# with no label

# 


