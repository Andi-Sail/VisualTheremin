import socket

class ThereminCommunication:

    UDP_IP_VISUAL = "piar.local"
    UDP_IP_AUDIO =  "ESKTOP-A4L73LO.local"
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
        self.pitchSock.bind((self.UDP_IP_VISUAL, self.UDP_PORT_PITCH))
        self.volSock.bind((self.UDP_IP_VISUAL, self.UDP_PORT_VOL))

    def connect(self):
        self.pitchSock.connect((self.UDP_IP_AUDIO, self.UDP_PORT_PITCH))
        self.pitchSock.connect((self.UDP_IP_AUDIO, self.UDP_PORT_VOL))

    def sendPitch(self, pitch):
        self.pitchSock.sendto(bytearray(str(pitch), 'utf-8'), (self.UDP_IP_AUDIO, self.UDP_PORT_PITCH))

    def sendVol(self, vol):
        self.pitchSock.sendto(bytearray(str(vol), 'utf-8'), (self.UDP_IP_AUDIO, self.UDP_PORT_VOL))

