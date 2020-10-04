#!/bin/bash

# Logging arguments
# -l oder --log -> Logging on
DEBUG="1"
if [ "$1" == "--log" ] || [ "$1" == "-l" ]
then
  DEBUG="1"
  echo $DEBUG
fi

#set path variable
CURDIR=$(pwd)
HOMEDIR=/home/pi/ASU
LOGFILE=$HOMEDIR/logs/ASU.log

# create log file if it does not exist
if [ "$DEBUG" == "1" ]
then
  touch $LOGFILE
  #date +%r-%-d/%-m/%-y >> $LOGFILE
  date +"%d.%m.%Y %T" >> $LOGFILE
fi

# Das Pin als Eingang definieren
if [ "$DEBUG" == "1" ]
then
echo "Define GPIO" | tee -a $LOGFILE 
fi
echo "19" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio19/direction

# Read Input 
previous=$(cat /sys/class/gpio/gpio19/value)
echo "Read Input" | tee -a $LOGFILE 

# Loop
while true
do
  # Den Zustand des Eingangs lesen
  pin=$(cat /sys/class/gpio/gpio19/value)

  # Wenn der Eingang von 0 auf 1 gewechselt hat
  if [ $pin -gt $previous ]
  then
    # Start Motor_script
    echo "Start Motor_script" | tee -a $LOGFILE 
    sudo bash /home/pi/ASU/ASU_V1.py
  else
    # Eine halbe Sekunde schlafen, damit der Prozessor nicht heissläuft
    sleep 0.5
  fi

  # Der aktuelle Wert wird der alte Wert für den nächsten Durchlauf
  previous=$pin
done
