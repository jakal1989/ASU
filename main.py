#Import diffrent libraries
import datetime
import sys
import time

import RPi.GPIO as GPIO

#Turn ON/OFF logs
Debug = False 
#LOG start script
if Debug == True: 
    old_stdout = sys.stdout
    log_file = open("/home/pi/ASU/logs/ASU.log","a")
    sys.stdout = log_file
    
#Define Variabelfor Datetime
now = datetime.datetime.now()

#disable warnings when Pin is already in use
GPIO.setwarnings(False)

#referring to the pins by the "Broadcom SOC channel"
GPIO.setmode(GPIO.BCM)

#Define PIN 21 as IN GPIO (Lightsensor)
GPIO.setup(21, GPIO.IN) 
#Define PIN 27 as IN GPIO (Stop button)
GPIO.setup(27, GPIO.IN) 

#import Classes
from led import Led
from motor import Motor
from mail import Mail
from rest import Rest
from sim import Sim
from file import File
	
################################################################################
# Program

if GPIO.input(21) == 1:
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    Motor.position_check()
    File.delete()
    dark = True
    #Loop
    while dark:
        if GPIO.input(21) == 1 and GPIO.input(27) == 0:
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            Led.green_on()
            Motor.position_check()
            print ("SIM in tray")
            Sim.read_on()
            Rest.post()
            Motor.run()
            
        elif GPIO.input(21) == 1 and GPIO.input(27) == 1:
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            print ("stoped by hand")
            Led.green_off()
            Led.red_on()
            Led.yellow_on()
            Mail.hand_stop()
            time.sleep(3)
            Led.red_off()
            Led.yellow_off()
            File.delete()
            Motor.stop()
            dark = False
            
        else:
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            print ("All SIM-Cards ejected from tray")
            Led.yellow_on()
            Mail.with_sim()
            time.sleep(3)
            Led.green_off()
            Led.yellow_off()
            File.delete()
            Motor.stop()
            dark = False
else:
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print ("No SIM-Card in tray")
    Motor.position_check()
    Led.red_on()
    time.sleep(3)
    Led.yellow_on()
    Mail.without_sim()
    time.sleep(3)
    Led.red_off()
    Led.yellow_off()
    Motor.stop()
        
#Stop LOG Script
if Debug == True:  
    sys.stdout = old_stdout
    log_file.close()