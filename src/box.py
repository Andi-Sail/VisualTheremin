import cv2
import colorFinder as cf

class box:
    width = 0
    height = 0
    space = 20
    thickness = 2

    def __init__(self, width, height, space = 20, thickness = 2):
        self.width = width
        self.height = height
        self.space = space
        self.thickness = thickness

        # Top left corner of rectangle
        self.start_point_vol = (self.space, self.space)
        
        # Bottom right corner of rectangle
        self.end_point_vol = ( int(self.width/4), (self.height - self.space))
      

        # Top left corner of rectangle
        self.start_point_pitch = (int((self.width/4) + self.space), int(self.height - self.height/2.5))

        # Bottom right corner of rectangle
        self.end_point_pitch = ( (self.width - self.space), (self.height - self.space))


    def drawBoxes(self, frame):
  
        ### Makes Vertical Box 
        # Blue color in BGR
        color1 = (255, 0, 0)
        cv2.rectangle(frame, self.start_point_vol, self.end_point_vol, color1, self.thickness)

        ### Makes Horizontal Box        
        # Blue color in BGR
        color2 = (255, 0, 0)            
        cv2.rectangle(frame, self.start_point_pitch, self.end_point_pitch, color2, self.thickness)

        return frame

    def getVolPitchSection(self, frame):
        volSection = frame[self.start_point_vol[1]:self.end_point_vol[1], self.start_point_vol[0]:self.end_point_vol[0]]
        pitchSection = frame[self.start_point_pitch[1]:self.end_point_pitch[1], self.start_point_pitch[0]:self.end_point_pitch[0]]

        return volSection, pitchSection

    def transformPointsToFrame(self, pointsVol, pointsPitch):
        points = list()

        for p in pointsVol:
            points.append(cf.Point(p.x + self.start_point_vol[0], p.y + self.start_point_vol[1]))

        for p in pointsPitch:
            points.append(cf.Point(p.x + self.start_point_pitch[0], p.y + self.start_point_pitch[1]))

        return points

    def getVolBoxHeight(self):
        return self.end_point_vol[1] - self.start_point_vol[1]

    def getPitchBoxWidth(self):
        return self.end_point_pitch[0] - self.start_point_pitch[0]

   