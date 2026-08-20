import numpy as np
import cv2

capture = cv2.VideoCapture('/home/kakon/Screencasts/aaaaa.webm')

while capture.isOpened():
    ret, frame = capture.read()

    if not ret:
        break

    width = 880
    height = 480
    frame_resized = cv2.resize(frame, (width, height))

    #grayframe
    grayframe = cv2.cvtColor(frame_resized,cv2.COLOR_BGR2GRAY)

    dark_mask = grayframe < 50
    dark_pixels = grayframe[dark_mask]    

    #print(f"dark pixel number: (len{dark_pixels}) ")
    cv2.imshow('Original Input Video', frame_resized)
    cv2.imshow('Processed video:',grayframe)

    cv2.moveWindow('Original Input Video', 50, 100)
    cv2.moveWindow('Processed Output Video', 710, 1000)

    #print("press any key to stop")

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()    