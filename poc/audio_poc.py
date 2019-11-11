import pyautogui as pag
import psonic as ps

maxPitch = 90
minPitch = 40

maxVol = 4
minVol = .1

pitch = minPitch
vol=minVol

def setPitch(p):
    global pitch
    pitch = p

def setVol(v):
    global vol
    vol = v

#screenSize = pag.size()
#width = screenSize[0]
#height = screenSize[1]

def play():
    global vol
    global pitch
    print("making music")

    while True:
        #pos = pag.position()
        #x = pos[0]
        #y = pos[1]

        #ps.use_synth(ps.DULL_BELL)
        #pitch = x*(maxPitch-minPitch)/width + minPitch
        #vol = y*(maxVol-minVol)/height + minVol

        #print (str(x) + " " + str(y) + '\r')


        ps.play(pitch, sustain=.05, attack=.05, release=.05, amp=vol)
        ps.sleep(.05)

