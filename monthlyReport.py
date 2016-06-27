import smtplib
import email.mime.text
import syslog

class monthlyCheck:
	def monthlyReport(self):
		self.variable = "Hello world"
		with open("batteryLogData.txt", 'r') as myFile:
			self.data = myFile.read()
		open("batteryLogData.txt", 'w').close()		

	
	def exportInfo(self):
	# print("APC Battery charge is at 50 percent. It is recommended that you check the battery ASAP!")
	# syslog.openlog('[UPS]')
	# def log(msg):
	#         syslog.syslog(str(msg))

		GMAIL_ADDRESS = 'Spikeyhedgehog141@gmail.com'
		GMAIL_PASSWORD = 'smtrout141'

		from_email = GMAIL_ADDRESS
		to_emails = ["jlittle@stanford.edu"]

		msg_subject = "REPORT: Monthly Report from APC Battery"
		msg_text = "The following information below concerns the APC Battery in room PP2. Take a quick look at the data and make sure that battery voltage and charge remain constant throughout the month. \n \n %s" % self.data 

		# log(msg_subject)

		msg = email.mime.text.MIMEText(msg_text)
		msg['Subject'] = msg_subject
		msg['From'] = from_email
		msg['To'] = ", ".join(to_emails)

		s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
		s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
		s.sendmail(from_email, to_emails, msg.as_string())
		s.quit()



	# def exportInfo(self):
	# 	print(self.data)


# m = monthlyCheck()
# m.monthlyReport()
# m.exportInfo()