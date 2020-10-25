#Importiere Bibliothek
import RPi.GPIO as GPIO

#Benutzung von "Broadcom SOC channel" PIN-Schema
GPIO.setmode(GPIO.BCM)
#Definiere PIN 23 als Ausgang GPIO (Led Grün)
GPIO.setup(23, GPIO.OUT)
#Definiere PIN 24 als Ausgang GPIO (Led Gelb)
GPIO.setup(24, GPIO.OUT)
#Definiere PIN 25 als Ausgang GPIO (Led Rot)
GPIO.setup(25, GPIO.OUT)

# Nur Zwei Methoden wurde beschrieben da die restlichen gleich aufgebaut sind
# Klasse Namens Led definieren
class Led:
    # Statische Methode Namens green_on() definieren
    @staticmethod
    def green_on():
        print ("Led green on")
        # Grüne Led einschalten
        GPIO.output(23, GPIO.HIGH)
    # Statische Methode Namens green_off() definieren
    @staticmethod    
    def green_off():
        print ("Led green off")
        # Grüne Led ausschalten
        GPIO.output(23, GPIO.LOW)
    @staticmethod    
    def yellow_on():
        print ("Led yellow on")
        GPIO.output(24, GPIO.HIGH)
    @staticmethod    
    def yellow_off():
        print ("Led yellow off")
        GPIO.output(24, GPIO.LOW)
    @staticmethod   
    def red_on():
        print ("Led red on")
        GPIO.output(25, GPIO.HIGH)
    @staticmethod    
    def red_off():
        print ("Led red off")
        GPIO.output(25, GPIO.LOW)
