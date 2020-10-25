#!/usr/bin/env python
#Bibliotheken importieren
import RPi.GPIO as GPIO
import time
import os

#disable warnings when Pin is already in use
GPIO.setwarnings(False)

#referring to the pins by the "Broadcom SOC channel"
GPIO.setmode(GPIO.BCM)

#Define PIN 21 as IN GPIO (Lightsensor)
GPIO.setup(19, GPIO.IN)

#Starte Schlaufe zum auslesen des PINs
while True:
    #Wenn Taster gedrückt wird
    if GPIO.input(19) == 1:
        #Starten von main Programm in Terminal
        os.system("sudo python3 /home/pi/ASU/main.py")
    #Wenn Taster nicht gedrückt wird    
    else:
        #Pause definieren um den Prozess nicht heisslaufen zu lassen
        time.sleep(0.5)