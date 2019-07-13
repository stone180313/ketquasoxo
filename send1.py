import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config
def send():
    
    gmailpassword = config.gmailpassword
    mailto = input("NHAP DIA CHI EMAIL MUON GUI \n ")
    tieude = input("TIEU DE BAN MUON GUI \n ")
    noidung = input("NOI DUNG BAN MUON GUI \n ")

    # msg1 = input("What is your message? \n ")
    msg = MIMEMultipart()
    msg['From'] = 'jangmi110985@gmail.com'
    msg['To'] = 'ledanghongphuc@gmail.com'
    msg['Subject'] = tieude
    msg.attach(MIMEText(noidung,'plain'))
    text = msg.as_string()

    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login('jangmi110985@gmail.com' , gmailpassword)
    mailServer.sendmail('jangmi110985@gmail.com', 'ledanghongphuc@gmail.com' , text)
    print(" \n Sent!")
    mailServer.quit()
send()