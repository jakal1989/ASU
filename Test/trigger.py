#!/usr/bin/env python
#Bibliotheken importieren
import RPi.GPIO as GPIO
import time
import os

# Schalte Warnungen aus wenn PIN schon in gebrauch ist
GPIO.setwarnings(False)

# Benutzung von "Broadcom SOC channel" PIN-Schema
GPIO.setmode(GPIO.BCM)

# Definiere PIN 19 als Eingang GPIO (Start Knopf)
GPIO.setup(19, GPIO.IN)

# Starte Schlaufe zum auslesen des PINs
while True:
    # Wenn Taster gedrückt wird
    if GPIO.input(19) == 1:
        # Starten von main Programm in Terminal
        os.system("sudo python3 /home/pi/ASU/main.py")
    # Wenn Taster nicht gedrückt wird    
    else:
        # Ansonsten eine halbe Sekunde warten und Schlaufe von vorne beginne.
        time.sleep(0.5)
