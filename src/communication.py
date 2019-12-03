import socket

class ThereminCommunication:

    # definitions for hostname / ip and port
    UDP_IP_VISUAL = "piar.local"            # hostname or ip for visual.py
    UDP_IP_AUDIO =  "DESKTOP-A4L73LO.local" # hostname or ip for audio.py
    UDP_PORT_PITCH = 5005                   # port to send pitch
    UDP_PORT_VOL = 5006                     # port to send volume

    pitchSock = None
    volSock = None

    # init sockets for UDP communication
    def __init__(self):
        self.pitchSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.volSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def bind(self):
        self.pitchSock.bind((self.UDP_IP_AUDIO, self.UDP_PORT_PITCH))
        self.volSock.bind((self.UDP_IP_AUDIO, self.UDP_PORT_VOL))

    def connect(self):
        self.pitchSock.connect((self.UDP_IP_AUDIO, self.UDP_PORT_PITCH))
        self.pitchSock.connect((self.UDP_IP_AUDIO, self.UDP_PORT_VOL))

    # sends the given pitch to the audio module
    def sendPitch(self, pitch):
        self.pitchSock.sendto(bytearray(str(pitch), 'utf-8'), (self.UDP_IP_AUDIO, self.UDP_PORT_PITCH))

    # sends the given volume to the audio module
    def sendVol(self, vol):
        self.pitchSock.sendto(bytearray(str(vol), 'utf-8'), (self.UDP_IP_AUDIO, self.UDP_PORT_VOL))

