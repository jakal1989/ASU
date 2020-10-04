import RPi.GPIO as gpio
import time

servoPIN = 17
servoPositions = [2.5,5,7.5,10,12.5]

def setServoCycle (p, position):
    p.ChangeDutyCycle(position)
    
    time.sleep(0.5)


try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)
    p.start(servoPositions[2.5])
    
    
  while True:
      for pos in servoPositions:
          setServocycle(p, 2.5)
          
      for pos in reversed (servoPositions):
          setServoCycle(p, 12.5)
          
except Keyboardinterrupt
    p.stop()
    GPIO.cleanup()