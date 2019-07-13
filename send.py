import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import config
def sendemail(noidung,msg):
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.ehlo()
        mailServer.starttls
        mailServer.login(config.EMAIL,config.PASSWORD)
        message = 'noidung: {}\n\n{}'.format(noidung,msg)
        mailto = 'ledanghongphuc@gmail.com'
        mailServer.sendmail(config.EMAIL,mailto,message)
        mailServer.quit()
        print('Da gui thanh cong')
    except:
        print('Email bi loi roi')

# https://myaccount.google.com/lesssecureapps
tieude =' helo python'
noidung = ' email cua python'

sendemail(tieude,noidung)