from __future__ import absolute_import, print_function, unicode_literals
import time
import itertools
import json
import urllib2
import requests
import ast
 
from streamparse.spout import Spout

class PowerSpout(Spout):
    
    # initializes the spout parameter values
    def initialize(self, stormconf, context):
        self.server_url = "http://127.0.0.1:8080"

    def next_tuple(self):
        # get power values for all sockets + format them properly
        raw_socketsdata= requests.get(self.server_url).content
        prepared_socketsdata=ast.literal_eval(raw_socketsdata)
        
        # for each socket values + prepare them + send them to the powerbolt
        for socketdata in prepared_socketsdata:
            socket = socketdata["mac"]
            power = float(socketdata["power"])
            email = socketdata["email"]
            threshold = socketdata["threshold"]
            self.emit([socket,power,email,threshold])
        
        # waits for 3 seconds before the next data request
        time.sleep(3)