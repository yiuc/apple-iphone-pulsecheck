#!/usr/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import os
import iphoneconfig

def sendGmailSmtp(strGmailUser,strGmailPassword,strRecipient,strSubject,strContent):
    strMessage = MIMEMultipart()
    strMessage['From'] = strGmailUser
    strMessage['To'] = strRecipient
    strMessage['Subject'] = strSubject
    strMessage.attach(MIMEText(strContent))
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(strGmailUser, strGmailPassword)
    mailServer.sendmail(strGmailUser, strRecipient, strMessage.as_string())
    mailServer.close()
    return 'send successed'

data = list(open(iphoneconfig.log_data,"r"))
stringdata = ""
for s in data:
    stringdata += s
print sendGmailSmtp(iphoneconfig.emailgatewayID,iphoneconfig.emailpwd,iphoneconfig.systememail,'Daily Iphone6 Log', stringdata)
os.remove(iphoneconfig.log_data)
