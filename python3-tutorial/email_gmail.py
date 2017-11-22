import smtplib
# has to setup 2-step authentication first, get the app password. personal password won't work; https://support.google.com/accounts/answer/185833
# ------------------------------------------------------------------- #
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login("incrediblechang@gmail.com", "app_password")
 
# msg = "YOUR MESSAGE! FROM PYTHON3"
# server.sendmail("incrediblechang@gmail.com", "chang.weicheng@gmail.com", msg)
# server.quit()

# ------------------------------------------------------------------- #

# from email.MIMEMultipart import MIMEMultipart # python2
# from email.MIMEText import MIMEText # python2

from email.mime.multipart import MIMEMultipart # python3
from email.mime.text  import MIMEText # python3

gmailUser = 'incrediblechang@gmail.com'
gmailPassword = 'qginuoenrnkzqiqf'
recipient = 'chang.weicheng@gmail.com'
message='your message here '

msg = MIMEMultipart()
msg['From'] = gmailUser
msg['To'] = recipient
msg['Subject'] = "Subject of the email python3"
msg.attach(MIMEText(message))

mailServer = smtplib.SMTP('smtp.gmail.com', 587)
mailServer.ehlo() #The SMTP server you're connecting to requires a sort of 'handshake' for the service to work properly. This is done using the .ehlo() function of smtplib.
mailServer.starttls() # As Google doesn't use SSL, we need to kick off TLS Encryption manually.
mailServer.ehlo()
mailServer.login(gmailUser, gmailPassword)
mailServer.sendmail(gmailUser, recipient, msg.as_string())
mailServer.close() # Finally, disconnect from the SMTP server when complete.