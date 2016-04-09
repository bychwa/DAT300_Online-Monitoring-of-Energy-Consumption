from __future__ import absolute_import, print_function, unicode_literals
import time
import itertools
import json
import urllib2
import requests
import ast
 
from streamparse.spout import Spout

class PowerSpout(Spout):

    def initialize(self, stormconf, context):
        self.sleep_time = 1 

    def next_tuple(self):
        data= requests.get('http://127.0.0.1:8080').content
        dataset=ast.literal_eval(data)
        if len(dataset)==0:
    	    self.emit(["0",0,"jacksonisack@gmail.com","100"])
        else:
	    for d in dataset:
                socket = d["mac"]
                power = float(d["power"])
                email = d["email"]
                threshold = d["threshold"]
                self.emit([socket,power,email,threshold])
        time.sleep(self.sleep_time)
