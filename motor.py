import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#Define PIN 17 as OUT GPIO (Servomotor)
GPIO.setup(17, GPIO.OUT)
#Define Name and PWM (50Hz)for PIN 17,
servo = GPIO.PWM(17,50)

class Motor:
    @staticmethod
    def run():
        # Start Motor
        # Cycle 2.5 = 0 degrees / 5 = 45 degrees / 7.5 = 90 degrees / 10 = 135 degrees / 12.5 = 180 degrees
        # start PWM running, check if Servo is set to 180
        print ("Set Servo to 180 degrees (Slider out of tray)")
        servo.start(12.5) # Initialisierung
        time.sleep(2.5)
        print ("Set Servo to 109 degrees (Slider in tray)")
        servo.ChangeDutyCycle(8.0)
        time.sleep(2.5)
        print ("Turning back to 180 degrees (Slider out of tray)")
        servo.ChangeDutyCycle(12.5)
        time.sleep(4.0)
    @staticmethod
    def position_check():
        # Set motor to 180 degees if in last run, an Error appeard an motor is no out of tray
        print ("Set Servo to 180 degrees (Check if Servo is out of tray)")
        servo.start(12.5) # Initialisierung
        time.sleep(2.5)
    @staticmethod   
    def stop():
        servo.stop()
        print ("Stop Motor")
        GPIO.cleanup()