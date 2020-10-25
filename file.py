#Importiere Bibliothek
import os

#Klasse Namens File definieren
class File:
    #Statische Methode Namens delete() definieren
    @staticmethod    
    def delete():
        print ("Delete Update list")
        # Wenn Update_list.txt exisitert diese löschen ansonsten Ausgabe in Konsole Datei existiert nicht
        if os.path.exists("Update_list.txt"):
          os.remove("Update_list.txt")
        else:
          print("The Update_list.txt file does not exist")
