import time

class FpsCounter:

    frameCounter = 0
    t = 0
    fps = 0
    windowSize = 10

    def __init__(self, windowSize=20):
        self.t = time.process_time()
        self.windowSize = windowSize

    # should be called for every frame
    def newFrame(self):
        self.frameCounter+=1
        if (self.frameCounter >= self.windowSize):
            self.frameCounter = 0
            elapsed_time = time.process_time() - self.t
                
            if (elapsed_time > 0):
                self.fps = self.windowSize/(elapsed_time)

            self.t = time.process_time()

    def getFps(self):
        return self.fps