import cv2

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

    def drawBoxes(self, frame):
        # Top left corner of rectangle
        start_point1 = (self.space, self.space)
        
        # Bottom right corner of rectangle
        end_point1 = ( int(self.width/4), (self.height - self.space))
        
        # Blue color in BGR
        color1 = (255, 0, 0)
        
        cv2.rectangle(frame, start_point1, end_point1, color1, self.thickness)

        ### Makes Horizontal Box
        
        # Top left corner of rectangle
        start_point2 = (int((self.width/4) + self.space), int(self.height - self.height/2.5))

        # Bottom right corner of rectangle
        end_point2 = ( (self.width - self.space), (self.height - self.space))

        # Blue color in BGR
        color2 = (255, 0, 0)
            
        cv2.rectangle(frame, start_point2, end_point2, color2, self.thickness)

        return frame
      

   