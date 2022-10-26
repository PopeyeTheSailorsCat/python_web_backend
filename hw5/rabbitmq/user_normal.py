import pika
import json
import logging


#
# params = pika.ConnectionParameters(host='localhost', port=5672)
# connection = pika.BlockingConnection(params)
#
# channel = connection.channel()


def get_msg(working_channel) -> bytes:
    method_frame, properties, msg = next(working_channel.consume('agency_normal_que'))
    working_channel.basic_ack(method_frame.delivery_tag)
    return msg


def get_telegram_msg(working_channel) -> bytes:
    method_frame, properties, msg = next(working_channel.consume('agency_normal_telegram_que'))
    working_channel.basic_ack(method_frame.delivery_tag)
    return msg


def app_process():
    params = pika.ConnectionParameters(host='localhost', port=5672)
    connection = pika.BlockingConnection(params)

    channel = connection.channel()
    telegram_channel = connection.channel()
    try:
        while True:
            obj = json.loads(get_msg(channel).decode('utf-8'))
            logging.warning(f"Normal msg to users: We found {obj['name']} with cost: {obj['cost']}")

            obj = json.loads(get_telegram_msg(telegram_channel).decode('utf-8'))
            logging.warning(f"Telegram msg:We found {obj['name']} with cost: {obj['cost']}")
        # br?eak
    except KeyboardInterrupt:
        channel.close()
        telegram_channel.close()


if __name__ == "__main__":
    app_process()
