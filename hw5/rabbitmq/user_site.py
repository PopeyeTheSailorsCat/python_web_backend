import pika
import json
import logging

params = pika.ConnectionParameters(host='localhost', port=5672)
connection = pika.BlockingConnection(params)

channel = connection.channel()


def get_msg_email(working_channel) -> bytes:
    method_frame, properties, msg = next(working_channel.consume('agency_site_email'))
    working_channel.basic_ack(method_frame.delivery_tag)
    return msg


def get_msg_user(working_channel) -> bytes:
    method_frame, properties, msg = next(working_channel.consume('agency_site_user'))
    working_channel.basic_ack(method_frame.delivery_tag)
    return msg


def app_process():
    params = pika.ConnectionParameters(host='localhost', port=5672)
    connection = pika.BlockingConnection(params)

    user_channel = connection.channel()
    email_channel = connection.channel()

    try:
        while True:
            obj = json.loads(get_msg_email(email_channel).decode('utf-8'))
            logging.warning(f"Email msg: We found {obj['name']} with cost: {obj['cost']}")

            obj = json.loads(get_msg_user(user_channel).decode('utf-8'))
            logging.warning(f"Online user msg: We found {obj['name']} with cost: {obj['cost']}")
        # br?eak
    except KeyboardInterrupt:
        user_channel.close()
        email_channel.close()


if __name__ == "__main__":
    app_process()
