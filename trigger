#!/bin/bash

# Pfadvariablen setzen
CURDIR=$(pwd)
HOMEDIR=/home/pi/ASU

# Definiere PIN 19 als Eingang
echo "Define GPIO"
echo "19" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio19/direction

# Lese Eingang 
previous=$(cat /sys/class/gpio/gpio19/value)
echo "Read Input" 

# Schlaufe ausführen um Eingang auszulesen
while true
do
  # Den Zustand des Eingangs lesen
  pin=$(cat /sys/class/gpio/gpio19/value)

  # Wenn der Eingangszustand wechselt Python Programm starten
  if [ $pin -gt $previous ]
  then 
    echo "Knopf wurde gedrückt"
    sudo python3 $HOMEDIR/main.py
  # Ansonsten eine halbe Sekunde warten und Schlaufe von vorne beginne.
  else
    sleep 0.5
  fi
  # Der aktuelle Wert wird der alte Wert für den nächsten Durchlauf
  previous=$pin
done
