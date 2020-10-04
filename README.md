# ASU
Automatic Sim-Card Updater

Das Tool wird verwendet um ein Servomotor zu steuern, der Automtisch eine SIMKarte aus einem ablagefach auswirft.
Hierbei wird ein Taster als starter des Programms verwendet sowie ein Lichtsensor welcher erkennt ob eine SIM-Karte im Fach ist.

Um das hier geschriebene Programm nutzen zu können müssen noch einige Anforderungen erfült werden.

1.  Benötigte Hardware 

    * 1x Raspberry Pi: V3 aufwärts
    * 1x [Servomotor (50Hz)](https://www.play-zone.ch/de/deservo-20kg-cm-digital-servo-ds3218mg.html)
    * 2x Taster: Keine Vorgabe
    * 1x [Lichtsensor](https://www.digitec.ch/de/s1/product/lichtsensor-sensor-elektronikmodul-8193992)
    * 1x SD-Karte(min 16GB): Keine Vorgabe
    * 10x Schrauben M3 mit Unterlagsscheiben und Mutter
    * 1x 0.5 mm Blech ca 20x30 cm
    * 1x Winkelstange Alu 1x0.5 cm ca. 50 cm Lang
    * 1x Holzkiste ca. 30x15x10 cm
    * 5x Klemmen für drähte
    * 1x Led Grün/Gelb/Rot
    * 1x 330 Ohm wiederstand
    * 1x Ausgedrucktes Ablagefach 3D. STL-File in attachements verfügbar.
    * [Jumperkabel](https://www.play-zone.ch/de/jumperkabel-verbindungskabel-10-20cm-50-stk-24awg.html)

2.  Installiere Rasbian auf deine SD Karte [Howto.](https://jankarres.de/2012/08/raspberry-pi-raspbian-installieren/)

3.  Der Ordner mit dazugehörigen files unter /home/pi ablegen.
    
4.  Die Trigger file muss mit der richtigen Berechtigungen versehen werden.

    ```sudo chmod 755 /home/pi/ASU/trigger```

5.  Autostart konfigurieren
    Der Autostart erfolgt über /etc/rc.local.
    
    ```sudo nano /etc/rc.local```
    
    In dieser File vor dem exit 0 folgende Zeile einsetzen:
    
    ```/home/pi/ASU/trigger &```
    
6.  ASU_V1.py mit texeditor öffnen und Email Absender mit dazugeörigem SMTP server definieren. 
    Sowie empfänger definieren.

7.  Anschliessen von Kabel an GPIOs
    
	![GPIO](https://workshop-iot-programming.devbit.be/assets/img/pinout_wiring_pi.56491fd7.png)
	
    * GPIO:BCM 19 Input Taster
    * GPIO.BCM 17 Output PWM Servo
    * GPIO.BCM 21 Input Lightsensor
    * GPIO.BCM 23 Output Grüne Led
    * GPIO.BCM 24 Output Gelbe Led
    * GPIO.BCM 25 Output Rote Led
    
    Der Servo muss an eine exterene Stromquelle angeschlossen werden, da dieser zu viel Strom verbraucht und der Raspberry zum abstürtzen bringt. 
    Ein 5V Ladegerät mit min. 1A Ausgang sollte reichen. Der Ground vom Ladegerät muss noch an den Ground des Raspberry Pi angeschlossen werden. 
    
    
    
