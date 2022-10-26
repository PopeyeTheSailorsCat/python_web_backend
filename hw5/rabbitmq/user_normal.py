import pika
import json
import logging


#
# params = pika.ConnectionParameters(host='localhost', port=5672)
# connection = pika.BlockingConnection(params)
#
# channel = connection.channel()


def get_msg(working_channel) -> bytes:
    _, _, msg = next(working_channel.consume('agency_normal_que'))
    return msg


def get_telegram_msg(working_channel) -> bytes:
    _, _, msg = next(working_channel.consume('agency_normal_telegram_que'))
    return msg


def app_process():
    params = pika.ConnectionParameters(host='localhost', port=5672)
    connection = pika.BlockingConnection(params)

    channel = connection.channel()
    telegram_channel = connection.channel()
    while True:
        obj = json.loads(get_msg(channel).decode('utf-8'))
        logging.warning(f"Normal msg to users: {obj}")

        obj = json.loads(get_telegram_msg(telegram_channel).decode('utf-8'))
        logging.warning(f"Telegram msg: {obj}")
        # br?eak


if __name__ == "__main__":
    app_process()
