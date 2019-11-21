import socket

class ThereminCommunication:

    UDP_IP_VISUAL = "piar.local"            # hostname or ip for visual.py
    UDP_IP_AUDIO =  "DESKTOP-A4L73LO.local" # hostname or ip for audio.py
    UDP_PORT_PITCH = 5005
    UDP_PORT_VOL = 5006

    pitchSock = None
    volSock = None

    def __init__(self):
        self.pitchSock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

        self.volSock = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP

    def bind(self):
        self.pitchSock.bind((self.UDP_IP_AUDIO, self.UDP_PORT_PITCH))
        self.volSock.bind((self.UDP_IP_AUDIO, self.UDP_PORT_VOL))

    def connect(self):
        self.pitchSock.connect((self.UDP_IP_AUDIO, self.UDP_PORT_PITCH))
        self.pitchSock.connect((self.UDP_IP_AUDIO, self.UDP_PORT_VOL))

    def sendPitch(self, pitch):
        self.pitchSock.sendto(bytearray(str(pitch), 'utf-8'), (self.UDP_IP_AUDIO, self.UDP_PORT_PITCH))

    def sendVol(self, vol):
        self.pitchSock.sendto(bytearray(str(vol), 'utf-8'), (self.UDP_IP_AUDIO, self.UDP_PORT_VOL))

