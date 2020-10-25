#!/usr/bin/env python
# Importieren von verschidenen Bibliotheken
import RPi.GPIO as GPIO
import time
import sys
import datetime

# Logs Ein-/Aus-schalten
Debug = False
# Log Start Skript: Logdatei anlegen Konsole Ausgabe in Datei schreiben mit mit Anhäng-Modus (Append)
if Debug == True: 
    old_stdout = sys.stdout
    log_file = open("/home/pi/ASU/logs/ASU.log","a")
    sys.stdout = log_file
    
# Instanziere Zeitstempel
now = datetime.datetime.now()

# Schalte Warnungen aus wenn PIN schon in gebrauch ist
GPIO.setwarnings(False)

# Benutzung von "Broadcom SOC channel" PIN-Schema
GPIO.setmode(GPIO.BCM)

# Definiere PIN 21 als Eingang GPIO (Lichtsensor)
GPIO.setup(21, GPIO.IN) 
# Definiere PIN 27 als Eingang GPIO (Stopp Knopf)
GPIO.setup(27, GPIO.IN) 

# importiere Klassen
from led import Led
from motor import Motor
from mail import Mail
from rest import Rest
from sim import Sim
from file import File
	
################################################################################
# Programm, die genauen beschreibungen der Methoden findet man in den Klassen

if GPIO.input(21) == 1:
    # Zeitstempel in Konsole ausgeben
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    Motor.position_check()
    File.delete()
    # Boolesche gleichung dark auf True stellen
    dark = True
    # Schlaufe reagiert auf die Boolesche gleichung dark = True
    while dark:
        # Wenn Lichtsenosr Dunkel erkennt und Stopp Taster nicht gedrückt wird dieser weg eingeschlagen 
        if GPIO.input(21) == 1 and GPIO.input(27) == 0:
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            Led.green_on()
            Motor.position_check()
            print ("SIM in tray")
            Sim.read_on()
            Rest.post()
            Motor.run()
        # Wenn Lichtsenosr Dunkel erkennt und Stopp Taster gedrückt wird dieser weg eingeschlage    
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
            # Boolesche gleichung Dark auf False stellen um aus der schlaufe zu gehen
            dark = False
        # Wenn Lichtsenosr Hell erkennt und Stopp Taster nicht gedrückt wird dieser weg eingeschlage    
        else:
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            Led.green_off()
            Led.red_on()
            print ("All SIM-Cards ejected from tray")
            Led.yellow_on()
            Mail.with_sim()
            time.sleep(3)
            Led.red_off()
            Led.yellow_off()
            File.delete()
            Motor.stop()
            # Boolesche gleichung Dark auf False stellen um aus der schlaufe zu gehen
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
        
# Beende das Logscript.
if Debug == True:  
    sys.stdout = old_stdout
    log_file.close()
