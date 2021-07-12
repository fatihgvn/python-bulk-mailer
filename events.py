import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cryptography.fernet import Fernet
from email_validator import validate_email, EmailNotValidError

def sendMail(title, message, settings, receiver):

    msg = MIMEMultipart('alternative')

    context = ssl.create_default_context()
    with smtplib.SMTP(settings['server'], int(settings['port']), timeout=30) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(settings['mail'], settings['passwd'])

        for m in receiver:
            msg['Subject'] = title
            msg['From'] = settings['mail']
            msg['To'] = m['mail']
            try:
                parts = MIMEText(message, 'plain')
                server.sendmail(settings['mail'], m['mail'], parts.as_string())
                yield {
                    "status": True,
                    "message": "sended mail -> {}".format(m['mail'])
                    }
            except Exception as ex:
                yield {
                    "status": False,
                    "a": ex,
                    "message": "send error -> {}".format(m['mail'])
                    }

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)


def checkmail(email):
    try:
        valid = validate_email(email)
        return valid
    except EmailNotValidError as e:
        return False 