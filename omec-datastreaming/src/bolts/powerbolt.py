from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import requests

class PowerCounter(Bolt):
    
    # initialises TotalPower and counter object
    def initialize(self, conf, ctx):
        self.TotalPower = Counter()
        self.PowerIterations=Counter()

    # processes each value received from the power-spout
    def process(self, tup):
        # tup - contain values from the power-spout
        socket = tup.values[0]
        power = tup.values[1]
        email = tup.values[2]
        threshold = tup.values[3]

        # TotalPower power values + TotalPower iterations
        self.TotalPower[socket] += power
        self.PowerIterations[socket] += 1
            
        self.emit([socket, self.TotalPower[socket]])
            
        # checks if the iterations == 5 then sends the average values to the database for storing
        if self.PowerIterations[socket]%5==0:
            average=self.TotalPower[socket]/self.PowerIterations[socket]
            data= requests.get('http://api.bawalab.com/omec/add_readings?mac='+str(socket)+'&power='+str(average))
        
        # checks if the socket has exceeded set threshold then notifies the user    
        if float(self.TotalPower[socket]) >= float(threshold):
            data= requests.get('http://api.bawalab.com/omec/notify?mac='+str(socket)+'&power='+str(self.TotalPower[socket]))
            self.log('%s: %d -- Alarm ' % (socket, self.TotalPower[socket]))
        else:    
            self.log('%s: %d' % (socket, self.TotalPower[socket]))
