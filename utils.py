import smtplib
from os import path

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import config


def mail_sender(
        recipients: list[str],
        data_to_send: str,
        subject: str = 'Здарова',
        filename_attachment: str = None,
):
    SERVER = config.SMTP_SERVER
    PASSWORD = config.TOKEN_API
    USER = config.USER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f'Python data from <{USER}>'
    # msg['To'] = 'test_hillel_api_mailing@ukr.net, w.i.k.mailua@gmail.com'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    if filename_attachment:
        file_exists = path.exists(filename_attachment)
        if not file_exists:
            print('File not exists')
        else:
            basename = path.basename(filename_attachment)
            filesize = path.getsize(filename_attachment)
            file = MIMEBase('application', f'octet-stream; name={basename}')
            file.set_payload(open(filename_attachment, 'rb').read())
            file.add_header('Content-Description', filename_attachment)
            file.add_header('Content-Description', f'attachment; filename={filename_attachment}; size={filesize}')
            encoders.encode_base64(file)
            msg.attach(file)

    text_to_send = MIMEText(data_to_send, 'plain')
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SERVER)
    mail.login(USER, PASSWORD)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


if __name__ == '__main__':
    recipients = [
        'test_hillel_api_mailing@ukr.net',
    ]

    mail_sender(data_to_send='text to ', recipients=recipients,  filename_attachment='utils.py')
