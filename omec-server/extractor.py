#!/usr/bin/python
import plugwise
from plugwise import Circle
from plugwise import Stick
import time

class PlugwiseOperator():

    def __init__(self, port,mac):
        stick = Stick(port)
        self.socket = Circle(mac, stick)
        self.socketActive = True
        self.socketUsage = 0

    def setStatus(self,status):
        if status == "true":
            self.socket.switch_on()
        else:
            self.socket.switch_off()
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
        
    def getData(self):
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