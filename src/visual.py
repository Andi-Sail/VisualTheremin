# main script for the image recognition of the visual Theremin
import colorFinder as cf
import cv2
import fpsCounter
import socket
import communication as com
import definitions as defs
import box

sender = com.ThereminCommunication()
sender.connect()

# get image capture object
cap = cv2.VideoCapture(0)
fps = fpsCounter.FpsCounter()

width = int(cap.get(3)) # float
height = int(cap.get(4)) # float
print("This Video Resulation is " + str(width) + " by " + str(height))

boxer = box.box(width, height)

while(True):    
    # Capture frame-by-frame
    fps.newFrame()
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # TODO: crop image section and compute points from sections
    # example to crop:         img_section = img[y:y+h, x:x+w]
    points = cf.findColor(frame, 'red', False)

    # draw found point in to original frame
    for p in points:
        cv2.circle(frame, (p.x, p.y), 5, (255, 255, 255), -1)

    # show frames per second on image
    fpsS = "fps: " + "{:5.2f}".format(fps.getFps())
    cv2.putText(frame, fpsS, (width - 100, 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    frame = boxer.drawBoxes(frame)

    # show current image
    cv2.imshow('frame',frame) 

    # send pitch and volume
    if (len(points) > 0):
        pitch = points[0].x*(defs.maxPitch-defs.minPitch)/width + defs.minPitch
        vol = points[0].y*(defs.maxVol-defs.minVol)/height + defs.minVol
        sender.sendPitch(pitch)
        sender.sendVol(vol)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()