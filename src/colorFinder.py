import numpy as np
import cv2


# holds x y coordinates in an image
class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

def getBWMask(frame, color):
    mask = None

    # Converts images from BGR to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    if color == 'red':
        # Range for lower red
        lower_red = np.array([0,130,125])
        upper_red = np.array([5,255,255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        
        # Range for upper range
        lower_red = np.array([175,130,125])
        upper_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv,lower_red,upper_red)
        
        # Generating the final mask to detect red color
        mask = mask1+mask2
    elif color == 'blue':
        # Range for blue
        lower_blue = np.array([110,130,125])
        upper_blue = np.array([130,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

    return mask

def findColor(frame, color='red'):

    onPi = False        # weather the code is run on the raspberry pi or a windows computer

    pointList = list()

    # apply average filter to blur the image and remove nois
    frame = cv2.blur(frame,(11,11))   
    #frame = cv2.GaussianBlur(frame,(11,11),0)

    cv2.imshow('frame filtered',frame) 
    cv2.waitKey(1)

    mask = getBWMask(frame, color)

    # find contours in the binary image
    contours = None
    if onPi:
        contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]
    else:
        contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        # calculate moments for each contour
        M = cv2.moments(c)
        
        # calculate x,y coordinate of center
        if not M["m00"] == 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"]) 
            pointList.append(Point(cX, cY))

    return pointList
  
