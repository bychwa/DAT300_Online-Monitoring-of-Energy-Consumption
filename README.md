## OMEC_DAT300-Project
App for Online Monitoring of Energy Consuption

# Introduction

Today's homes have seen an increase in the use of advanced metering infrastructure (AMI) and a move away from automatic meter reading (AMR) in metering devices such as electricity meters, gas meters, heat meters, and water meters. The adoption of AMI entails two way communication between the AMI systems and the metering devices for the purposes of measuring, collecting, and analyzing energy usage. This can be either on a request basis or in a scheduled manner.

In this project, we aim to look at the domestic online monitoring of energy consumption. A small ZigBee network will be setup by having a source sensor forwarding energy consumption information to a server sensor. The server will run a lightweight Stream Processing Engine prototype which will process this kind of information. We aim to take advantage of this capability by allowing the energy user(s) to set their own threshold energy usage value. Once this value is reached, the system will generate an “alarm” that can be sent to the user via email and/or SMS, notifying them that their usage has exceeded their desired usage preference.

# Demo
Demo for how the System works can be seen here

# Prerequisites
> 1. This system uses plugwise electric plugs and stick connect, collect and transfer socket power usage information. More info here
> 2. Odroid Microcontroller / Computer that contains linux operating system. More info here
> 3. Python 3
> 4. Streamparse. Python wrapper/implementation of the Storm Processing engine. More info here
> 5. IOS/Android tablet with OMEC App. Can be downloaded from here

# Installation
> 1. Download project code from here to your computer
> 2. SSH to Ordroid Device
> 3. Install Python, Lein, Streamparse and USB Drivers for the Plugwise doongle if you dont have them setup
> 4. Create a folder, name it whatever you prefer. Copy omec-datastreaming and omec-server you downloaded in step 1, inside that folder.
> 5. Copy omec-start.sh to insde the same folder as well.
> 6. Add execute permission to the omec-start.sh by running: chmod ugo+x omec-start.sh
> 7. run the project by executing this command: ./omec-start.sh
