import pika
import json
import logging


def get_msg(working_channel) -> bytes:
    method_frame, properties, msg = next(working_channel.consume('agency_premium_que'))
    working_channel.basic_ack(method_frame.delivery_tag)
    return msg


def app_process(running_test=False):
    params = pika.ConnectionParameters(host='localhost', port=5672)
    connection = pika.BlockingConnection(params)

    channel = connection.channel()
    try:

        while True:
            logging.warning("SOMETHING")
            obj = json.loads(get_msg(channel).decode('utf-8'))
            logging.warning(f"SPECIAL FOR YOU! We found {obj['name']} with cost: {obj['cost']}")
            if running_test:
                raise KeyboardInterrupt

    except KeyboardInterrupt:
        channel.close()


if __name__ == "__main__":
    app_process()
