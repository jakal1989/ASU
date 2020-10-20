import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.OUT)

class Sim:
    @staticmethod    
    def read_on():
        print ("Read SIM-Card")
        GPIO.output(11, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(11, GPIO.LOW)
        time.sleep(2)