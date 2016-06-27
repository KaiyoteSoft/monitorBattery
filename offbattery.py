#!/usr/bin/env python

import smtplib
import email.mime.text
import syslog

syslog.openlog('[UPS]')
def log(msg):
    syslog.syslog(str(msg))

GMAIL_ADDRESS = 'Spikeyhedgehog141@gmail.com'
GMAIL_PASSWORD = 'smtrout141'

from_email = GMAIL_ADDRESS
to_emails = ["jlittle@stanford.edu"]  # cell phone address

msg_subject = "OK: UPS Power Recovered"
msg_text = "Auto Notification"

log(msg_subject)

msg = email.mime.text.MIMEText(msg_text)
msg['Subject'] = msg_subject
msg['From'] = from_email
msg['To'] = ", ".join(to_emails)
s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
s.sendmail(from_email, to_emails, msg.as_string())
s.quit()
