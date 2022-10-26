import pika
import json
import logging


def get_msg(working_channel) -> bytes:
    _, _, msg = next(working_channel.consume('agency_premium_que'))
    return msg


def app_process():
    params = pika.ConnectionParameters(host='localhost', port=5672)
    connection = pika.BlockingConnection(params)

    channel = connection.channel()
    try:

        while True:
            obj = json.loads(get_msg(channel).decode('utf-8'))
            logging.warning(obj)
            # br?eak
    except KeyboardInterrupt:
        channel.close()


if __name__ == "__main__":
    app_process()
