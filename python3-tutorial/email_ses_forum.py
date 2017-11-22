#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText

#SES requires a header and a body in order to send an email
#the sender address has to be verified
 
# def prompt(prompt):
#     return raw_input(prompt).strip()

msg_body = """From: USER@FROM.COM
 
Hello, this is dog.
"""

print("Message length is " + repr(len(msg_body))) # changed to python3 format
msg = MIMEMultipart() # you know what it does
msg['Subject'] = "" # can be empty
msg.attach(MIMEText(msg_body))


fromaddr = 'incrediblechang@gmail.com'
toaddrs  = 'chang.weicheng@gmail.com'

 

 
#Change according to your settings
smtp_server = 'email-smtp.us-east-1.amazonaws.com'
smtp_username = 'AKIAIT2EFNM5SQ26FBIA'
smtp_password = 'ApMFvs4ZDP5PiUEtIO0wZC38WvilELCdygFdajDEXYON'
smtp_port = '587'
smtp_do_tls = True
 
server = smtplib.SMTP(
    host = smtp_server,
    port = smtp_port,
    timeout = 10
)
server.set_debuglevel(10)
server.ehlo() # not required; however stmplib docs recommend calling ehlo() before & after starttls()
server.starttls()
server.ehlo()
server.login(smtp_username, smtp_password)
server.sendmail(fromaddr, toaddrs, msg.as_string()) # now that msg is a dictionary
print(server.quit()) # changed to python3 format

