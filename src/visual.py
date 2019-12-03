# main script for the image recognition of the visual Theremin
import colorFinder as cf
import cv2
import fpsCounter
import socket
import communication as com
import definitions as defs
import box
import math

# init sender for pitch and volume
sender = com.ThereminCommunication()
sender.connect()

# get the camera
cap = cv2.VideoCapture(0)
fps = fpsCounter.FpsCounter()

# determine the image resolution
width = int(cap.get(3))
height = int(cap.get(4))
print("This Video Resulation is " + str(width) + " by " + str(height))

# init box with image resolution
boxer = box.box(width, height)

while(True):    
    # Capture new frame
    fps.newFrame()
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # get individual sections for pitch and volume
    volSection, pitchSection = boxer.getVolPitchSection(frame)

    # find colored points in each sections
    pointsVol = cf.findColor(volSection, 'red', False)
    pointsPitch = cf.findColor(pitchSection, 'red', False)

    # transform coordinates back to the full frame
    points = boxer.transformPointsToFrame(pointsVol, pointsPitch)

    # draw found point in to original frame
    for p in points:
        cv2.circle(frame, (p.x, p.y), 5, (255, 255, 255), -1)

    # show frames per second on image
    fpsS = "fps: " + "{:5.2f}".format(fps.getFps())
    cv2.putText(frame, fpsS, (width - 100, 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    # draw boxes on the image
    frame = boxer.drawBoxes(frame)

    # show current image
    cv2.imshow('frame',frame)

    # send new pitch and volume to audio module
    if (len(pointsPitch) > 0):
        pitch = pointsPitch[0].x*(defs.maxPitch-defs.minPitch)/boxer.getPitchBoxWidth() + defs.minPitch
        sender.sendPitch(pitch)

    if (len(pointsVol) > 0):
        vol = (math.e**(pointsVol[0].y / boxer.getVolBoxHeight()) -1) / (math.e-1) * (defs.maxVol-defs.minVol) + defs.minVol
        vol = defs.maxVol - vol
        sender.sendVol(vol)

    # check if user wants to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()