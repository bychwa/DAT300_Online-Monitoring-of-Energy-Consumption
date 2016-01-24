from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import requests

class PowerCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.counts_count=Counter()

    def process(self, tup):
        socket = tup.values[0]
        power = tup.values[1]
        email = tup.values[2]
        threshold = tup.values[3]

        self.counts[socket] += power
        self.counts_count[socket] += 1
            
        self.emit([socket, self.counts[socket]])
            
        #sending data for statistics
        if self.counts_count[socket]%5==0:
            average=self.counts[socket]/self.counts_count[socket]
            data= requests.get('http://api.bawalab.com/omec/add_readings?mac='+str(socket)+'&power='+str(average))
            
        if float(self.counts[socket]) >= float(threshold):
            data= requests.get('http://api.bawalab.com/omec/notify?mac='+str(socket)+'&power='+str(self.counts[socket]))
            self.log('%s: %d -- Alarm ' % (socket, self.counts[socket]))
        else:    
            self.log('%s: %d' % (socket, self.counts[socket]))
