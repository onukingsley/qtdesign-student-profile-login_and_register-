from passlib.hash import cisco_pix as ci
from passlib.hash import crypt16 as sa
from documentation import __version__
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def checkempty(arrays):
    msg = False
    for case in arrays:
        if not case:
            msg = True

    return msg

def cleartext(arrays):
    for items in arrays:
        items.setText("")


def encrypt(password):
    return sa.encrypt(password)

def verify(new, old):
    return sa.verify(new, old)

def sendemail(sendto="onu.nnamdi.2000@gmail.com", subject= "Message from CleanDom .ltd", message = "Wishing you a good and splendid day from us at CleanDom" ):
    mail = 'onu.kigsley.54@gmail.com'
    password = 'onunnamdikingsley'
    subject = subject
    message = message

    msg = MIMEMultipart()
    msg['From'] = mail
    msg['To'] =  sendto
    msg['subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    sever = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    sever.login(mail, password)
    text = msg.as_string()

    try:
        sever.sendmail(mail, sendto, text)
        feedback = 'ok'

    except Exception as err:
        feedback = f"""error: {err}"""

    return feedback

def emailSender(send_to="authcourse67@gmail.com", Subject="Mail from Our App",
                    Message="Default message been sent!"):
        mail = 'onu.kingsley.54@gmail.com'
        password = 'onunnamdikingsley'
        subject = Subject
        message = Message

        msg = MIMEMultipart()
        msg['From'] = "CLEANDOM"
        msg['To'] = send_to
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'html'))
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Secure using SSL

        server.login(mail, password)
        text = msg.as_string()

        try:
            server.sendmail(mail, send_to, text)
            msg = 'ok'
        except Exception as err:
            msg = f"Error: {err}"
        return msg
