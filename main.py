import schedule

import library


def main():

    schedule.every().monday.at('18:24').do(library.self_promotion)
    schedule.every().tuesday.at('07:15').do(library.self_promotion)
    schedule.every().wednesday.at('07:15').do(library.self_promotion)
    schedule.every().thursday.at('07:15').do(library.self_promotion)
    schedule.every().day.at('07:15').do(library.self_promotion)

    schedule.every(10).seconds.do(library.greeting)
    schedule.every().minute.at(':23').do(library.self_promotion)

    schedule.every(5).seconds.do(library.send_mail_to_me)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
