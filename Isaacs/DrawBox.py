# references:
#   https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/
#   https://stackoverflow.com/questions/51229126/how-to-find-the-red-color-regions-using-opencv
#   https://www.geeksforgeeks.org/detection-specific-colorblue-using-opencv-python/
#   https://www.learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(3)) # float
height = int(cap.get(4)) # float

print("This Video Resulation is " + str(width) + " by " + str(height))


while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()
        
    frame = cv2.flip(frame, 1)
    
    ### Makes Vertical Box
    space = 20      # Gives some space from the edge of the box
    
    # Top left corner of rectangle
    start_point1 = (space, space)
      
    # Bottom right corner of rectangle
    end_point1 = ( int(width/4), (height - space))
      
    # Blue color in BGR
    color1 = (255, 0, 0)
      
    # Line thickness of 2 px
    thickness1 = 2

    cv2.rectangle(frame, start_point1, end_point1, color1, thickness1)


      ### Makes Horizontal Box
     
    # Top left corner of rectangle
    start_point2 = (int((width/4) + space), int(height - height/2.5))

    # Bottom right corner of rectangle
    end_point2 = ( (width - space), (height - space))

    # Blue color in BGR
    color2 = (255, 0, 0)
        
    # Line thickness of 2 px
    thickness2 = 2


    cv2.rectangle(frame, start_point2, end_point2, color2, thickness2)
   
   
    cv2.imshow('frame',frame) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# Changes 
