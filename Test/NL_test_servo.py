# Servo1.py

import RPi.GPIO as GPIO
import time

P_SERVO = 11 # adapt to your wiring
fPWM = 50  # Hz (not higher with software PWM)
a = 12
b = 2

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_SERVO, GPIO.OUT)
    pwm = GPIO.PWM(P_SERVO, fPWM)
    pwm.start(0)

def setDirection(direction):
    duty = a / 360 * direction + b
    pwm.ChangeDutyCycle(duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(1) # allow to settle
   
print "starting"
setup()
for direction in range(0, 361, 10):
    setDirection(direction)
direction = 0    
setDirection(0)    
GPIO.cleanup() 
print "done"