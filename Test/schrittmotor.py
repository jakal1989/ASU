import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 24 # pink
coil_A_2_pin = 4 # orange
coil_B_1_pin = 23 # blau
coil_B_2_pin = 25 # gelb
coil2_A_1_pin = 18 # pink
coil2_A_2_pin = 22 # orange
coil2_B_1_pin = 17 # blau
coil2_B_2_pin = 27 # gelb

StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

GPIO.setup(coil2_A_1_pin, GPIO.OUT)
GPIO.setup(coil2_A_2_pin, GPIO.OUT)
GPIO.setup(coil2_B_1_pin, GPIO.OUT)
GPIO.setup(coil2_B_2_pin, GPIO.OUT)

def setStep(w1, w2, w3, w4):
 GPIO.output(coil_A_1_pin, w1)
 GPIO.output(coil2_A_1_pin, w1)
 GPIO.output(coil_A_2_pin, w2)
 GPIO.output(coil2_A_2_pin, w2)
 GPIO.output(coil_B_1_pin, w3)
 GPIO.output(coil2_B_1_pin, w3)
 GPIO.output(coil_B_2_pin, w4)
 GPIO.output(coil2_B_2_pin, w4)
 
def forward(delay, steps):
 for i in range(steps):
	for j in range(StepCount):
		setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
		time.sleep(delay)
		
def backwards(delay, steps):
 for i in range(steps):
	for j in reversed(range(StepCount)):
		setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
		time.sleep(delay)
		
delay = 1
steps = 512 # Ganze umdrehung 512 schritte
backwards(int(delay) / 1000.0, int(steps))
		

#delay = 1 
#steps = 200
#backwards/forward(int(delay) / 1000.0, int(steps))