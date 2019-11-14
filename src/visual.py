# main script for the image recognition of the visual Theremin
import colorFinder as cf
import cv2
import fpsCounter

# get image capture object
cap = cv2.VideoCapture(0)
fps = fpsCounter.FpsCounter()

while(True):    
    # Capture frame-by-frame
    fps.newFrame()
    ret, frame = cap.read()

    # TODO: crop image section and compute points from sections
    # example to crop:         img_section = img[y:y+h, x:x+w]
    points = cf.findColor(frame, 'red')

    # draw found point in to original frame
    for p in points:
        cv2.circle(frame, (p.x, p.y), 5, (255, 255, 255), -1)

    # show frames per second on image
    fpsS = "fps: " + "{:5.2f}".format(fps.getFps())
    cv2.putText(frame, fpsS, (25, 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    # show current image
    cv2.imshow('frame',frame) 

    # TODO compute pitch and volume from points. See example in poc/audio_poc.py

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()