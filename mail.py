import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

class Mail:
    @staticmethod
    def with_sim():
        #Send Email with Update_list.txt and update finished message
        print("Send E-Mail - with Update List (Update finished)")
        fromaddr = "asu.swisscom@gmail.com"
        toaddr = "stefano.cugis@gmail.com"
        smtppass = 'password'
        # instance of MIMEMultipart 
        msg = MIMEMultipart() 
        # storing the senders email address   
        msg['From'] = fromaddr 
        # storing the receivers email address  
        msg['To'] = toaddr 
        # storing the subject  
        msg['Subject'] = "ASU - INFO"
        # string to store the body of the mail 
        body = "Automatic SIM Update Finished"
        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 
        # open the file to be sent
        filename = "Update_list.txt"
        attachment = open("Update_list.txt", "rb")
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form 
        p.set_payload((attachment).read())
        # encode into base64 
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        # start TLS for security 
        s.starttls() 
        # Authentication 
        s.login(fromaddr, smtppass) 
        # Converts the Multipart msg into a string 
        text = msg.as_string() 
        # sending the mail 
        s.sendmail(fromaddr, toaddr, text)
    @staticmethod
    def hand_stop():
        #Send Email with Update_list.txt and Handstop message
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
        s.ehlo()
        s.starttls() 
        s.login(fromaddr, smtppass) 
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
    @staticmethod
    def without_sim():
        #Send Email without SIM
        print ("Send Email - no SIM in tray")
        fromaddr = 'asu.swisscom@gmail.com'
        toaddr = 'stefano.cugis@gmail.com'
        smtppass = 'password'
        subject = 'ASU - INFO'
        header = 'To: ' + toaddr + '\n' + 'From: ' + fromaddr + '\n' + 'Subject: ' + subject
        body = 'No SIM in tray'
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login(fromaddr, smtppass)
        s.sendmail(fromaddr, toaddr, header + '\n\n' + body)
    
