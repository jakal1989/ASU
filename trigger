#!/bin/bash

#set path variable
CURDIR=$(pwd)
HOMEDIR=/home/pi/ASU
LOGFILE=$HOMEDIR/logs/trigger.log

# define Pin as Input
echo "Define GPIO"
echo "19" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio19/direction

# Read Input 
previous=$(cat /sys/class/gpio/gpio19/value)
echo "Read Input" 

# Loop
while true
do
  # Den Zustand des Eingangs lesen
  pin=$(cat /sys/class/gpio/gpio19/value)

  # Wenn der Eingang von 0 auf 1 gewechselt hat
  if [ $pin -gt $previous ]
  then 
    echo "Knopf wurde gedrückt"
    sudo python3 $HOMEDIR/main.py
  else
    # Eine halbe Sekunde schlafen, damit der Prozessor nicht heissläuft
    sleep 0.5
  fi
  # Der aktuelle Wert wird der alte Wert für den nächsten Durchlauf
  previous=$pin
done
