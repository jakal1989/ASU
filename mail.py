#!/usr/bin/env python
#Importieren von verschidenen Bibliotheken
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

# Klasse Namens Mail definieren
class Mail:
    # Statische Methode Namens with_sim() definieren
    @staticmethod
    def with_sim():
        print("Send E-Mail - with Update List (Update finished)")
        # Senderadresse definieren
        fromaddr = "asu.swisscom@gmail.com"
        # Empfänger Adresse definieren
        toaddr = "stefano.cugis@gmail.com"
        # Passwort für Login bei Senderadresse
        smtppass = 'password'
        # instanzieren von MIMEMultipart und benne sie 'msg'
        msg = MIMEMultipart() 
        # speichern der Senderadresse  
        msg['From'] = fromaddr 
        # speichern der Empfängeradresse  
        msg['To'] = toaddr 
        # Betreff speichern 
        msg['Subject'] = "ASU - INFO"
        # Nachricht der E-Mail 
        body = "Automatic SIM Update Finished"
        # Füge die Nachricht der 'msg' Instanz hinzu 
        msg.attach(MIMEText(body, 'plain')) 
        # Öffne Update_list.txt
        filename = "Update_list.txt"
        attachment = open("Update_list.txt", "rb")
        # instanzieren von MIMEBase und bennene sie 'p'
        p = MIMEBase('application', 'octet-stream')
        # Nutzdaten in eine codierte Form ändern
        p.set_payload((attachment).read())
        # in base64 codierenen
        encoders.encode_base64(p)
        # Füge Header in Email mit Filemname und Dateianhang
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        # Füge die instanz 'p' der Instanz'msg' hinzu 
        msg.attach(p) 
        # SMTP-Sitzung erstellen
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        # sStarte TLS verschlüsselung 
        s.starttls() 
        # Authentifizierung (Login) 
        s.login(fromaddr, smtppass) 
        # Konvertiert die mehrteilige Nachricht in eine Zeichenfolge
        text = msg.as_string() 
        # Email senden 
        s.sendmail(fromaddr, toaddr, text)
    @staticmethod
    def hand_stop():
        print("Send E-Mail - with Update List (Handstop)")
        fromaddr = "asu.swisscom@gmail.com"
        toaddr = "stefano.cugis@gmail.com"
        smtppass = 'password'
        msg = MIMEMultipart()  
        msg['From'] = fromaddr   
        msg['To'] = toaddr   
        msg['Subject'] = "ASU - ERROR"
        body = "Automatic SIM-Card Updater stoped by Hand"
        msg.attach(MIMEText(body, 'plain')) 
        filename = "Update_list.txt"
        attachment = open("Update_list.txt", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p) 
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls() 
        s.login(fromaddr, smtppass) 
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
    @staticmethod
    def without_sim():
        print ("Send Email - no SIM in tray")
        fromaddr = 'asu.swisscom@gmail.com'
        toaddr = 'stefano.cugis@gmail.com'
        smtppass = 'password'
        subject = 'ASU - INFO'
        header = 'To: ' + toaddr + '\n' + 'From: ' + fromaddr + '\n' + 'Subject: ' + subject
        body = 'No SIM in tray'
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, smtppass)
        s.sendmail(fromaddr, toaddr, header + '\n\n' + body)
