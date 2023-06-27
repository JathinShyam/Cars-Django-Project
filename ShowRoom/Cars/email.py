from email.message import EmailMessage

import smtplib

def sendemail(data1):

    sender_email="youremail@email.com"
    sender_password="password"
    receiver_email="any mail"

    msg=EmailMessage()
    msg.set_content(data1)

    msg['Subject']= "Car data details \n"
    msg['From']= sender_email
    msg['To']= receiver_email

    server= smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,sender_password)
    server.send_message(msg)
    server.quit()