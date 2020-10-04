#!/usr/bin/python

import subprocess
 
wert = subprocess.Popen(['python /home/pi/light_sensor.py'], stdout=subprocess.PIPE)
stdout = process.communicate()
wert = stdout.decode('utf-8').split('\n')[1])
if (wert = '1')
   then
           echo "Start Motor Script" | tee -a $LOGFILE
            sudo bash start.sh
fi
 

 