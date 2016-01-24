#!/usr/bin/python
import extractor
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from extractor import PlugwiseOperator
import requests
import json
import urllib2
		

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	def json_list(list):
	    lst = []
	    d = {}
	    for pn in list:
	        d['mpn']=pn
	        lst.append(d)
	    return json.dumps(lst, separators=(',',':'))
	#Handler for the GET requests
	def do_GET(self):
		
		getValues=[]
		sockets = json.load(urllib2.urlopen('http://api.bawalab.com/omec/all_sockets'))
		for socket in sockets:
			mac=socket['mac']
			stick="/dev/ttyUSB0"
			po=PlugwiseOperator(stick,str(mac))
			soc_power=po.getData()
			# po.setStatus(socket['active'])
			row={}
			row['mac']=mac
			row['power']=soc_power
			row['email']=socket['email']
			row['threshold']=socket['threshold']
			getValues.append(row)
			
		# print json.dumps(getValues, separators=(',',':'))
		print getValues

		self.send_response(200)
		self.send_header('Content-type','application/json')
		self.end_headers()
		# Send the html message
		self.wfile.write(getValues)

		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()

