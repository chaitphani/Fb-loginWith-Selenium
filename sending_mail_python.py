import smtplib, ssl

port = 465

smtp_server = 'smtp.gmail.com'

sender_email = input("Enter your mail id: ")

password = input("Enter your password: ")

print('that"s grt there is one step more')

reciever_email = input('Enter the reciever email to send a mail: ')


message = '''\
Subject: Hi there

Chusindhi chalu, pani cheyi....
'''

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message)
