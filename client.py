import requests
import time
import ast

while True:
	data= requests.get('http://127.0.0.1:8081').content
	dataset=ast.literal_eval(data)       
	print dataset
	time.sleep(2)
