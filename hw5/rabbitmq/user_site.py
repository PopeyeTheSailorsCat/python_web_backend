import pika
import json
import logging

params = pika.ConnectionParameters(host='localhost', port=5672)
connection = pika.BlockingConnection(params)

channel = connection.channel()


def get_msg_email(working_channel) -> bytes:
    _, _, msg = next(working_channel.consume('agency_site_email'))
    return msg


def get_msg_user(working_channel) -> bytes:
    _, _, msg = next(working_channel.consume('agency_site_user'))
    return msg


def app_process():
    params = pika.ConnectionParameters(host='localhost', port=5672)
    connection = pika.BlockingConnection(params)

    user_channel = connection.channel()
    email_channel = connection.channel()
    while True:
        obj = json.loads(get_msg_email(email_channel).decode('utf-8'))
        logging.warning(f"Email msg: {obj}")

        obj = json.loads(get_msg_user(user_channel).decode('utf-8'))
        logging.warning(f"Online user msg: {obj}")
        # br?eak


if __name__ == "__main__":
    app_process()
