# Importieren von verschidenen Bibliotheken
import requests
import datetime
import time

#Instanziere Zeitstempel
now = datetime.datetime.now()

class Rest:
    # Statische Methode Namens post() definieren
    @staticmethod
    def post():
        # Rest Post von Postman
        print ("Rest Post send")
        # Zeitstempel in Update_list.txt schreiben mit Anhäng-Modus (Append)
        print (now.strftime("%Y-%m-%d %H:%M:%S"), file=open('Update_list.txt', 'a'))
        # Anfrage an Postmanserver mit Post request
        url = "https://f910d01a-4731-411c-8275-ce56ded1ec7e.mock.pstmn.io/post/"
        # Welchen Request man machen möchte
        payload = {'Update': 'post'}
        # Falls man datein anfordern möchte müsste man dies hier machen
        files = []
        # Mitgeschickter header
        headers = {'Device': 'ASU'}
        # Aufbau der Antwort die man erhält
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        # Antwort von Restserver in Update_list.txt schreiben mit Anhäng-Modus (Append)
        print(response.text.encode('utf8'), file=open('Update_list.txt', 'a'))
        print ("Rest Post saved answer in Update_list")
        # Warte 10 sekunden
        time.sleep(10)
