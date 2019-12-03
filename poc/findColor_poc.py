# references:
#   https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/
#   https://stackoverflow.com/questions/51229126/how-to-find-the-red-color-regions-using-opencv
#   https://www.geeksforgeeks.org/detection-specific-colorblue-using-opencv-python/
#   https://www.learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/


import numpy as np
import cv2
import time
import _thread
import audio_poc as a

onPi = False

_thread.start_new_thread ( a.play, () )

cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#cap.set(cv2.CAP_PROP_BRIGHTNESS, 1)
#cap.set(cv2.CAP_PROP_CONTRAST, 1)
#cap.set(cv2.CAP_PROP_SATURATION, 1)
#cap.set(cv2.CAP_PROP_WB_TEMPERATURE, 45)

width = 640
height = 480

frameCounter=0
t = time.process_time()
fps = 0

while(True):
    if (frameCounter >= 10):
        frameCounter = 0
        elapsed_time = time.process_time() - t
            
        if (elapsed_time > 0):
            fps = 10/(elapsed_time)
        t = time.process_time()

    frameCounter+=1

    # Capture frame-by-frame
    ret, frame = cap.read()

    #kernelAverage = np.ones((5,5),np.float32)/25
    #frame = cv2.filter2D(frame,-1,kernelAverage)
    frame = cv2.blur(frame,(11,11))   


    # Converts images from BGR to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    # Range for lower red
    lower_red = np.array([0,160,125])
    upper_red = np.array([5,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    # Range for upper range
    lower_red = np.array([175,160,125])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    
    # Generating the final mask to detect red color
    mask = mask1+mask2
    
    # Range for blue
    #lower_blue = np.array([110,130,125])
    #upper_blue = np.array([130,255,255])
    #mask = cv2.inRange(hsv, lower_blue, upper_blue)
  
    # find contours in the binary image
    contours = None
    if onPi:
        contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]
    else:
        contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # calculate moments for each contour
        #c = np.array(c)
        #print (c, type(c))
        M = cv2.moments(c)
        
        # calculate x,y coordinate of center
        if not M["m00"] == 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
            cv2.putText(frame, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)   

            a.pitch = cX*(a.maxPitch-a.minPitch)/width + a.minPitch
            a.vol = cY*(a.maxVol-a.minVol)/height + a.minVol     

    # The bitwise and of the frame and mask is done so  
    # that only the blue coloured objects are highlighted  
    # and stored in res 
    res = cv2.bitwise_and(frame,frame, mask= mask) 

    fpsS = "fps: " + str(fps)
    #print(fpsS)
    cv2.putText(frame, fpsS, (25, 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

