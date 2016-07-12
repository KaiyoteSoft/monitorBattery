import smtplib
import email.mime.text
import syslog

class warningCheck:
	def monthlyReport(self):
		with open("batteryLogData.txt", 'r') as myFile:
			self.data = myFile.read()
		# for line in reversed(open("batteryLogData.txt").readlines()):
		# 	self.data.append(line.rstrip())
			# print(self.data)

	def warningMessage75(self):
		print("APC Battery charge is at 75 percent. It is recommended that you check the battery and replace if needed.")
		syslog.openlog('[UPS]')
		def log(msg):
		        syslog.syslog(str(msg))

		GMAIL_ADDRESS = 'Spikeyhedgehog141@gmail.com'
		GMAIL_PASSWORD = 'smtrout141'

		from_email = GMAIL_ADDRESS
		# to_emails = ["jlittle@stanford.edu"]
		to_emails = ["kaioda141@gmail.com"]

		msg_subject = "WARNING: APC Battery Health Low"
		msg_text = "APC Battery charge is at 75 percent. It is recommended that you check the battery and replace if needed. Here is the most recent daily battery data: \n \n %s" % self.data

		log(msg_subject)

		msg = email.mime.text.MIMEText(msg_text)
		msg['Subject'] = msg_subject
		msg['From'] = from_email
		msg['To'] = ", ".join(to_emails)

		s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
		s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
		s.sendmail(from_email, to_emails, msg.as_string())
		s.quit()

	def warningMessage(self):
		print(self.data)
		print("APC Battery charge is at 50 percent. It is recommended that you check the battery ASAP!")
		syslog.openlog('[UPS]')
		def log(msg):
		        syslog.syslog(str(msg))

		GMAIL_ADDRESS = 'Spikeyhedgehog141@gmail.com'
		GMAIL_PASSWORD = 'smtrout141'

		from_email = GMAIL_ADDRESS
		# to_emails = ["jlittle@stanford.edu"]
		to_emails = ["kaioda141@gmail.com"]

		msg_subject = "WARNING: APC Battery Health Declining"
		msg_text = "APC Battery charge in Room PP2 is at 50 percent. It is recommended that you check the battery ASAP! Here is the most recent daily battery data: \n \n %s" % self.data

		log(msg_subject)

		msg = email.mime.text.MIMEText(msg_text)
		msg['Subject'] = msg_subject
		msg['From'] = from_email
		msg['To'] = ", ".join(to_emails)

		s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
		s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
		s.sendmail(from_email, to_emails, msg.as_string())
		s.quit()

	def warningMessage20(self):
		print("APC Battery charge is at 20 percent. Shutdowns and loss of data are imminent.")
		syslog.openlog('[UPS]')
		def log(msg):
		        syslog.syslog(str(msg))

		GMAIL_ADDRESS = 'Spikeyhedgehog141@gmail.com'
		GMAIL_PASSWORD = 'smtrout141'

		from_email = GMAIL_ADDRESS
		# to_emails = ["jlittle@stanford.edu"]
		to_emails = ["kaioda141@gmail.com"]

		msg_subject = "DANGER: APC Battery Health FAILING"
		msg_text = "APC Battery charge is at 20 percent. Shutdowns and loss of data are imminent. Here is the most recent daily battery data: \n \n %s" % self.data

		log(msg_subject)

		msg = email.mime.text.MIMEText(msg_text)
		msg['Subject'] = msg_subject
		msg['From'] = from_email
		msg['To'] = ", ".join(to_emails)

		s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
		s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
		s.sendmail(from_email, to_emails, msg.as_string())
		s.quit()

