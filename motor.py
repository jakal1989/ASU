#!/usr/bin/env python
# Importieren von verschidenen Bibliotheken
import RPi.GPIO as GPIO
import time

# Benutzung von "Broadcom SOC channel" PIN-Schema
GPIO.setmode(GPIO.BCM)

# Definiere PIN 17 als Ausgang GPIO (Motor)
GPIO.setup(17, GPIO.OUT)
# Instanziere GPIO 17 mit dem Namen servo und bestimme Frequenz 50Hz
servo = GPIO.PWM(17,50)

# Klasse Namens Motor definieren
class Motor:
    # Statische Methode Namens run() definieren
    @staticmethod
    def run():
        print ("Set Servo to 180 degrees (Slider out of tray)")
        # Warte 2.5 Sekunden
        time.sleep(2.5)
        # Initialisierung setzte den Motor auf 180 Grad
        servo.start(12.5)
        # Warte 2.5 Sekunden
        time.sleep(2.5)
        print ("Set Servo to 99 degrees (Slider in tray)")
        # Setzte den Motor auf 99 Grad
        servo.ChangeDutyCycle(8.0)
        # Warte 2.5 Sekunden
        time.sleep(2.5)
        print ("Turning back to 180 degrees (Slider out of tray)")
        # Setzte den Motor auf 180 Grad
        servo.ChangeDutyCycle(12.5)
         # Warte 4 Sekunden
        time.sleep(4.0)
    # Statische Methode Namens positions_check() definieren
    @staticmethod
    def position_check():
        print ("Set Servo to 180 degrees (Check if Servo is out of tray)")
        # Warte 2.5 Sekunden
        time.sleep(2.5)
        # Initialisierung setzte den Motor auf 180 Grad
        servo.start(12.5)
        # Warte 2.5 Sekunden
        time.sleep(2.5)
    # Statische Methode Namens stop() definieren
    @staticmethod   
    def stop():
        # Motor anhalten und auf Null stellen
        servo.stop()
        print ("Stop Motor")
        # Alle Pins auf Null stellen
        GPIO.cleanup()
