# references:
#   https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/
#   https://stackoverflow.com/questions/51229126/how-to-find-the-red-color-regions-using-opencv
#   https://www.geeksforgeeks.org/detection-specific-colorblue-using-opencv-python/

import numpy as np
import cv2
import time


cap = cv2.VideoCapture(0)

while(True):
    t = time.process_time()

    # Capture frame-by-frame
    ret, frame = cap.read()

    kernelAverage = np.ones((5,5),np.float32)/25
    frame = cv2.filter2D(frame,-1,kernelAverage)


    # Converts images from BGR to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    # Range for lower red
    lower_red = np.array([0,150,125])
    upper_red = np.array([5,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    # Range for upper range
    lower_red = np.array([175,150,125])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    
    # Generating the final mask to detect red color
    mask = mask1+mask2
  
    # find contours in the binary image
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        # calculate moments for each contour
        M = cv2.moments(c)
        
        # calculate x,y coordinate of center
        if not M["m00"] == 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
            cv2.putText(frame, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)        

    # The bitwise and of the frame and mask is done so  
    # that only the blue coloured objects are highlighted  
    # and stored in res 
    res = cv2.bitwise_and(frame,frame, mask= mask) 

    elapsed_time = time.process_time() - t
    fps = float('inf')
    if (elapsed_time > 0):
        fps = 1/(elapsed_time)
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

