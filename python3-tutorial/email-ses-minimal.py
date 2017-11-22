import smtplib
#import email.utils
from email.mime.multipart import MIMEMultipart # python3
from email.mime.text  import MIMEText # python3

message='minimum setup' #can be empty

msg = MIMEMultipart() # now it's down to
# msg['From'] = gmailUser
# msg['To'] = recipient
msg['Subject'] = "" # can be empty
msg.attach(MIMEText(message))



server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
server.starttls()
server.login("AKIAIT2EFNM5SQ26FBIA", "ApMFvs4ZDP5PiUEtIO0wZC38WvilELCdygFdajDEXYON")
server.sendmail("incrediblechang@gmail.com", "chang.weicheng@gmail.com", msg.as_string())
server.quit()