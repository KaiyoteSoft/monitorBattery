!/bin/sh/env python
#
# This shell script if placed in /etc/apcupsd
# will be called by /etc/apcupsd/apccontrol when the UPS
# goes on batteries.
# We send an email message to root to notify him.
#

import smtplib
import email.mime.text
import syslog

syslog.openlog('[UPS]')
def log(msg):
        syslog.syslog(str(msg))

GMAIL_ADDRESS = 'Spikeyhedgehog141@gmail.com'
GMAIL_PASSWORD = 'smtrout141'

from_email = GMAIL_ADDRESS
to_emails = ["jlittle@stanford.edu"]

msg_subject = "WARNING: APC Battery Health Declining"
msg_text = "APC Battery charge is at 50 percent. It is reccomended that you check the battery ASAP!"

log(msg_subject)

msg = email.mime.text.MIMEText(msg_text)
msg['Subject'] = msg_subject
msg['From'] = from_email
msg['To'] = ", ".join(to_emails)

s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
s.sendmail(from_email, to_emails, msg.as_string())
s.quit()
