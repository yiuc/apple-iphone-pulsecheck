#!/usr/bin/python
import urllib2
import os
import smtplib
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime
import iphoneconfig

my_list = ["http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&option.dimensionColor=silver&option.dimensionCapacity=16gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&option.dimensionColor=silver&option.dimensionCapacity=64gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&option.dimensionColor=silver&option.dimensionCapacity=128gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&option.dimensionColor=gold&option.dimensionCapacity=16gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&option.dimensionColor=gold&option.dimensionCapacity=64gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&option.dimensionColor=gold&option.dimensionCapacity=128gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&option.dimensionColor=space_gray&option.dimensionCapacity=16gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&option.dimensionColor=space_gray&option.dimensionCapacity=64gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&option.dimensionColor=space_gray&option.dimensionCapacity=128gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6P?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&option.dimensionColor=silver&option.dimensionCapacity=16gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6P?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&option.dimensionColor=silver&option.dimensionCapacity=64gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6P?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&option.dimensionColor=silver&option.dimensionCapacity=128gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6P?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&option.dimensionColor=gold&option.dimensionCapacity=16gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6P?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&option.dimensionColor=gold&option.dimensionCapacity=64gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6P?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&option.dimensionColor=gold&option.dimensionCapacity=128gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6P?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&option.dimensionColor=space_gray&option.dimensionCapacity=16gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6P?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&option.dimensionColor=space_gray&option.dimensionCapacity=64gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED",
"http://store.apple.com/hk-zh/buyFlowSelectionSummary/IPHONE6P?node=home/shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&option.dimensionColor=space_gray&option.dimensionCapacity=128gb&option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED"]

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

def checkStock(iphonejson):
	isbuyable = iphonejson["body"]["content"]["selected"]["purchaseOptions"]["isBuyable"]
	if isbuyable == True:
		return iphonejson["body"]["content"]["selected"]["partNumber"]
	else:
		return ""
#
# read data
#
model_data = open(iphoneconfig.model_data)
store_data = open(iphoneconfig.store_data)
# model_data = open('iphone_model')
# store_data = open('store_map')
modeljson = json.load(model_data)
storejson = json.load(store_data)

#
# url is defined above.
#
haveStock = ""
for link in my_list:
	try:
		url = link
		response = urllib2.urlopen(link);
	except Exception, e:
		print datetime.datetime.now().isoformat() + ": %s" % e
		print sendGmailSmtp(iphoneconfig.emailgatewayID,iphoneconfig.emailpwd,iphoneconfig.systememail,'Error', "%s\n" %e + url)
		sys.exit(0)
	html=response.read()
	iphonejson = json.loads(html)
	phone = checkStock(iphonejson)
	if len(phone) > 0:
		haveStock += modeljson[phone]+"\n"+"http://store.apple.com/hk/buy-iphone/iphone6?cppart=UNLOCKED/WW&product="+phone+"&step=accessories\n"
if len(haveStock) > 0:
	print datetime.datetime.now().isoformat() + ": Online Stock haveStock: " + haveStock
	print sendGmailSmtp(iphoneconfig.emailgatewayID,iphoneconfig.emailpwd,iphoneconfig.receiveemail,'IPhone Stock avaliable', 'Go\n' + haveStock)
else:
	print datetime.datetime.now().isoformat() + ": Online No Stock"
