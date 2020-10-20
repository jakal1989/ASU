import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#Define PIN 23 as OUT GPIO (LED green)
GPIO.setup(23, GPIO.OUT)
#Define PIN 24 as OUT GPIO (LED yellow)
GPIO.setup(24, GPIO.OUT)
#Define PIN 25 as OUT GPIO (LED red)
GPIO.setup(25, GPIO.OUT)

class Led:
    # Class to turn on and off notification led
    @staticmethod
    def green_on():
        print ("Led green on")
        GPIO.output(23, GPIO.HIGH)
    @staticmethod    
    def green_off():
        print ("Led green off")
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