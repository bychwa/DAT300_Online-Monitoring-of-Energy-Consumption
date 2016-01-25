#!/usr/bin/python
import extractor
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from extractor import PlugwiseOperator
import requests
import json
import urllib2
    
#port number for the local server http service
PORT_NUMBER = 8080

#This class will handles any incoming request from
#the storm processing engine < more specifically, powerspout > 
class RequestHandler(BaseHTTPRequestHandler):
    

    #Handler for the GET requests
    def do_GET(self):
        
    	getValues=[]
    	# this gets a list of all current sockets from the online database
        sockets = json.load(urllib2.urlopen('http://api.bawalab.com/omec/all_sockets'))
    	
        for socket in sockets:
    	    mac=socket['mac']
    	    stick="/dev/ttyUSB0"
    	    # initialize plugwise operator object to make a call for power values
            po=PlugwiseOperator(stick,str(mac))
            # returns power value for a given socket
    	    soc_power=po.getPower()
            #toogles the socket state i.e switches ON or OFF
    	    po.setStatus(socket['active'])
    	    row={}
    	    row['mac']=mac
    	    row['power']=soc_power
    	    row['email']=socket['email']
    	    row['threshold']=socket['threshold']
    	    # adds values for each socket found above
            getValues.append(row)
    
        print getValues

        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        # Send the json message back to the powerspout that requested for it
        self.wfile.write(getValues)
        
        return

try:
    #Creates a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), RequestHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    # Waits forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()

