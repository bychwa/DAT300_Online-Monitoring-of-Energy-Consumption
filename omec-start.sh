#!/bin/bash
conf_route
clear
echo ">>>>  WELCOME TO OMEC SYSTEM <<<<"
sleep 3
echo "Starting up a server at port 8080"
python ~/Desktop/ict-project/omec-server/server.py &
sleep 2
echo "Starting up storm data processing"
cd ~/Desktop/ict-project/omec-datastreaming/
sparse run & 
cd ~/Desktop/ict-project/
