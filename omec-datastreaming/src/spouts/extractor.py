#!/usr/bin/python
import plugwise
from plugwise import Circle
from plugwise import Stick
import time
# import operator_module
# from operator_module import Operator


class PlugwiseOperator():
    def __init__(self, port):
        stick = Stick(port)
        self.socket1 = Circle('000D6F0001A44DE1', stick)
        self.socket2 = Circle('000D6F0001A44958', stick)
        self.socket1Active = True
        self.socket2Active = True
        self.socket1Usage = 0
        self.socket2Usage = 0

    def getData(self):
        data = []
        if self.socket1Active:
            try:
                pw1Usage = round(self.socket1.get_power_usage(), 2)
            except:
                print
                "socket1 not active"
                pw1Usage = 0
                self.socket1Active = False
        else:
            pw1Usage = 0

        if self.socket2Active:
            try:
                pw2Usage = round(self.socket2.get_power_usage(), 2)
            except:
                print
                "socket2 not active"
                pw2Usage = 0
        else:
            pw2Usage = 0

        pw1IsOn = "OFF"
        pw2IsOn = "OFF"
        if pw1Usage > 0.1:
            pw1IsOn = "ON"
            self.socket1Usage = pw1Usage
        else:
            pw1Usage = self.socket1Usage
        if pw2Usage > 0.1:
            pw2IsOn = "ON"
            self.socket2Usage = pw2Usage
        else:
            pw2Usage = self.socket2Usage
        data.append("1 " + str(pw1Usage * 10) + " " + str(pw1IsOn) + " " + str(time.time()))
        data.append("2 " + str(pw2Usage * 10) + " " + str(pw2IsOn) + " " + str(time.time()))
        return data

    def run_ui(self):
        socket_choice = int(raw_input("Enter the socket to read:\n 1- Master socket \n 2- Slave socket\n "))
        input_action = int(raw_input("Enter\n 1- ON \n 2- OFF \n 3- Power Usage \n 4- Log\n "))

        s = Stick(port="/dev/ttyUSB0")

        mac1 = '000D6F0001A44DE1'
        mac2 = '000D6F0001A44958'

        c1 = Circle(mac1, s)
        c2 = Circle(mac2, s)

        while (1):
            if socket_choice == 1:
                c = c1;
            elif socket_choice == 2:
                c = c2;

            if input_action == 1:
                c.switch_on();
                break;

            elif input_action == 2:
                c.switch_off();
                break;

            elif input_action == 3:
                print
                c.get_power_usage();
                break;

            elif input_action == 4:
                print
                c.get_power_usage_history()
                break;

