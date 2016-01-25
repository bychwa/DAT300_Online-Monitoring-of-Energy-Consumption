#!/usr/bin/python
import plugwise
from plugwise import Circle
from plugwise import Stick

class PlugwiseOperator():

    #initializes the plugwise operator for a specific stick and doogle
    def __init__(self, port,mac):
        stick = Stick(port)
        self.socket = Circle(mac, stick)
        self.socketActive = True
        self.socketUsage = 0

    # toogles the socket state i.e if ON or OFF
    def setStatus(self,status):
        if status == "true":
            self.socket.switch_on()
        else:
            self.socket.switch_off()

    # returns the current state of the socket        
    def getStatus(self):
        if self.socketActive:
            try:
                pwUsage = round(self.socket.get_power_usage(), 2)
            except:
                print "socket not active"
                pwUsage = 0
                self.socketActive = False
        pwIsOn = "OFF"        
        if pwUsage > 0.1:
            pwIsOn = "ON"
            self.socketUsage = pwUsage
        else:
            pwUsage = self.socketUsage
        return pwIsOn
    
    #   returns power values of the socket  
    def getPower(self):
        if self.socketActive:
            try:
                pwUsage = round(self.socket.get_power_usage(), 2)
            except:
                print "socket not active"
                pwUsage = 0
                self.socketActive = False
        else:
            pwUsage = 0

        pwIsOn = "OFF"

        if pwUsage > 0.1:
            pwIsOn = "ON"
            self.socketUsage = pwUsage
        else:
            pwUsage = self.socketUsage
        return pwUsage