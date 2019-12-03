import psonic as ps
import socket
import communication as com
import _thread

vol=0
pitch=0

# init and bind reciever
receiver = com.ThereminCommunication()
receiver.bind()

def receivePitch():
    global receiver
    global pitch

    while True:
        data, addr = receiver.pitchSock.recvfrom(1024)
        pitch = float(data)
        print("new pitch: " + str(pitch))

def receiveVol():
    global receiver
    global vol

    while True:
        data, addr = receiver.volSock.recvfrom(1024)
        vol = float(data)
        print("new volume: " + str(vol))

# starts playing music - never returns
def play():
    global vol
    global pitch
    print("making music")

    while True:
        ps.play(pitch, sustain=.1, attack=.05, release=.05, amp=vol)
        ps.sleep(.1)


# recieve pitch asynchron
_thread.start_new_thread ( receivePitch, () )
# recieve volume asynchron
_thread.start_new_thread ( receiveVol, () )

play()