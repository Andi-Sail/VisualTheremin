import psonic as ps
import socket
import communication as com
import _thread

vol=0
pitch=0

receiver = com.ThereminCommunication()
receiver.bind()

def receivePitch():
    global receiver
    global pitch

    while True:
        data, addr = receiver.pitchSock.recvfrom(1024) # buffer size is 1024 bytes
        print("Recieved data" + str(data))
        pitch = float(data)
        print("new pitch: " + str(pitch))

def receiveVol():
    global receiver
    global vol

    while True:
        data, addr = receiver.volSock.recvfrom(1024) # buffer size is 1024 bytes
        print("Recieved data" + str(data))
        vol = float(data)
        print("new volume: " + str(vol))

def play():
    global vol
    global pitch
    print("making music")

    while True:
        ps.play(pitch, sustain=.05, attack=.05, release=.05, amp=vol)
        ps.sleep(.05)


_thread.start_new_thread ( receivePitch, () )
_thread.start_new_thread ( receiveVol, () )

play()