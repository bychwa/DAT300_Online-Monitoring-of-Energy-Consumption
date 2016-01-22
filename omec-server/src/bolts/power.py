from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt


class PowerCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        
        socket = tup.values[0]
        power = tup.values[1]
        
        self.counts[socket] += power

        self.emit([socket, self.counts[socket]])
        self.log('%s: %d' % (socket, self.counts[socket]))
