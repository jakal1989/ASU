#!/usr/bin/python3

#Import different libraries
import RPi.GPIO as GPIO
import time
import smtplib
import requests
import sys
import datetime

#old_stdout = sys.stdout
#log_file = open("ASU.log","w")
#sys.stdout = log_file
#now = datetime.datetime.now()
#print (now.strftime("%Y-%m-%d %H:%M:%S"))


GPIO.setwarnings(False)

#PIN Occupancy model, GPIO numbering
GPIO.setmode(GPIO.BCM)

#Define PIN 21 as IN GPIO (Lightsensor)
GPIO.setup(21, GPIO.IN)
#Define PIN 27 as IN GPIO (Stop button)
GPIO.setup(27, GPIO.IN)

#Define PIN 17 as OUT GPIO (Servomotor)
GPIO.setup(17, GPIO.OUT)
#Define Name and PWM (50Hz)for PIN 17,
servo = GPIO.PWM(17,50)

#Define PIN 23 as OUT GPIO (LED green)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)
GPIO.output(23, GPIO.LOW)
#Define PIN 24 as OUT GPIO (LED yellow)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.HIGH)
GPIO.output(24, GPIO.LOW)
#Define PIN 25 as OUT GPIO (LED red)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)
GPIO.output(25, GPIO.LOW)

#Define GPIO 11 as OUT GPIO (Relay SIM-Card reader)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)


class motor:
    @staticmethod
    def run():
        # Start Motor
        # Cycle 2.5 = 0 degrees / 5 = 45 degrees / 7.5 = 90 degrees / 10 = 13 degrees / 12.5 = 180 degrees
        # start PWM running, check if Servo is set to 180
        print ("Set Servo to 180 degrees (Slider out of tray)")
        servo.start(12.5) # Initialisierung
        time.sleep(2.5)
        print ("Set Servo to 108 degrees (Slider in tray)")
        servo.ChangeDutyCycle(8.5)
        time.sleep(2.5)
        print ("Turning back to 180 degrees (Slider out of tray)")
        servo.ChangeDutyCycle(12.5)
        time.sleep(4.0)
    @staticmethod
    def positioncheck():
        # Set motor to 180 degees if in last run, an Error appeard an motor is no out of tray
        print ("Set Servo to 180 degrees (Check if Servo is out of tray)")
        servo.start(12.5) # Initialisierung
        time.sleep(2.5)
    @staticmethod   
    def stop():
        servo.stop()
        print ("Stop Motor")
        GPIO.cleanup()

class led:
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

class email:
    @staticmethod
    def withsim():
        #Send Email with SIM
        print ("Send Email - Last SIM ejected")
        smtpUser = ''
        smtpPass = ''
        toAdd = ''
        fromAdd = smtpUser
        subject = 'ASU - INFO'
        header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
        body = 'Automatic SIM Update Finished'
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.login(smtpUser, smtpPass)
        s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
    @staticmethod
    def withoutsim():
        #Send Email without SIM
        print ("Send Email - no SIM in tray")
        smtpUser = ''
        smtpPass = ''
        toAdd = ''
        fromAdd = smtpUser
        subject = 'ASU - INFO'
        header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
        body = 'No SIM in tray'
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.login(smtpUser, smtpPass)
        s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
    @staticmethod
    def handstop():
        #Send Email without SIM
        print ("Send Email - handstop")
        smtpUser = ''
        smtpPass = ''
        toAdd = ''
        fromAdd = smtpUser
        subject = 'ASU - ERROR'
        header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
        body = 'ASU stoped by hand'
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.login(smtpUser, smtpPass)
        s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
    
class rest:
    @staticmethod
    def post():
        #Rest call als neue Klasse definieren
        print ("Rest Post send")
        url = "https://f910d01a-4731-411c-8275-ce56ded1ec7e.mock.pstmn.io/post/?ICCID=82816516156113284895152&Update=OK"
        payload = {'ICCID': '82816516156113284895152','Update': 'OK'}
        files = []
        headers = {'SnowPOS': 'Online'}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        print(response.text.encode('utf8'), file=open('Update_list.txt', 'a'))
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"), file=open('Update_list.txt', 'a'))
        print ("Rest Post saved answer in Upload_list")
        time.sleep(10)
        
class sim:
    @staticmethod    
    def read_on():
        print ("Read SIM-Card")
        GPIO.output(11, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(11, GPIO.LOW)
        time.sleep(2)
	
if GPIO.input(21) == 1:
    #Loop
    motor.positioncheck()
    dark = True
    while dark:
        if GPIO.input(21) == 1 and GPIO.input(27) == 0:
            led.green_on()
            motor.positioncheck()
            print ("SIM in tray")
            sim.read_on()
            rest.call()
            motor.run()
            
        elif GPIO.input(21) == 1 and GPIO.input(27) == 1:
            print ("stoped by hand")
            led.green_off()
            led.red_on()
            led.yellow_on()
            email.handstop()
            time.sleep(3)
            led.red_off()
            led.yellow_off()
            motor.stop()
            dark = False
            
        else:
            print ("All SIM-Cards ejected from tray")
            led.yellow_on()
            email.withsim()
            time.sleep(3)
            led.green_off()
            led.yellow_off()
            motor.stop()
            dark = False
else:
    print ("No SIM-Card in tray")
    led.red_on()
    time.sleep(3)
    led.yellow_on()
    email.withoutsim()
    time.sleep(3)
    led.red_off()
    led.yellow_off()
    GPIO.cleanup()
        
#sys.stdout = old_stdout

#log_file.close()
