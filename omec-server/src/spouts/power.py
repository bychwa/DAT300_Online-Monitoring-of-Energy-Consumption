from __future__ import absolute_import, print_function, unicode_literals
import time
import itertools
import json
import urllib2

        
from streamparse.spout import Spout

class PowerSpout(Spout):

    def initialize(self, stormconf, context):
	    self.words = itertools.cycle(['dog', 'cat',
                                      'zebra', 'elephant'])

    def next_tuple(self):
        powerValues = json.load(urllib2.urlopen('http://127.0.0.1:8080'))
        for dataset in powerValues:
            socket = dataset[0]
            power = float(dataset[1])
            self.emit([socket, power])
                    
        time.sleep(3)

        # r = requests.get("http://127.0.0.1:8080")
        # socketUsage=r.content.split(" ")
        
        
