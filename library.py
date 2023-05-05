import utils
import winsound


def send_mail_to_me():
    recipients = [
        'test_hillel_api_mailing@ukr.net',
    ]

    utils.mail_sender(data_to_send='Прокидайся, пора в школу', recipients=recipients)


def greeting():
    print('Wake up, lazy lizard!!!!!!!!')
    winsound.Beep(5000, 1000)


def self_promotion():
    print('You are simply the best')
