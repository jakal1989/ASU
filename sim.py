#!/usr/bin/env python
#Importieren von verschidenen Bibliotheken
import RPi.GPIO as GPIO
import time

#Benutzung von "Broadcom SOC channel" PIN-Schema
GPIO.setmode(GPIO.BCM)
#Definiere PIN 11 als Ausgang GPIO (Relais)
GPIO.setup(11, GPIO.OUT)

#Klasse Namens Sim definieren
class Sim:
    #Statische Methode Namens read_on() definieren
    @staticmethod    
    def read_on():
        print ("Read SIM-Card")
        #Relais Einschalten
        GPIO.output(11, GPIO.HIGH)
        #2 Sekunden warten
        time.sleep(2)
        #Relais Ausschalten
        GPIO.output(11, GPIO.LOW)
        #2 Sekunden warten
        time.sleep(2)
