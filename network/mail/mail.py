import smtplib

server = smtplib.SMTP('smtp-mail.outlook.com', 25)

server.ehlo()

server.login()