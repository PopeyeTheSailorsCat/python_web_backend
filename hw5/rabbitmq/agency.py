import pika
import time
import json
import logging
from hw5.rabbitmq.apartments import apartments_tread

params = pika.ConnectionParameters(host='localhost', port=5672)
connection = pika.BlockingConnection(params)


def send_apartment_to_clients(apartment_data: dict) -> None:
    """
    This function get the apartment_data and send it to right exchange
    :param apartment_data:
    :return:
    """

    channel = connection.channel()
    logging.info(f"Get new apartment:{apartment_data['name']}")
    ap_type = apartment_data['client']
    if ap_type == 'premium':
        logging.info("Publishing new apartments  to direct msg")
        channel.basic_publish(exchange='agency_premium', routing_key='some_premium_key',
                              body=json.dumps(apartment_data, indent=2).encode('utf-8'))
    elif ap_type == 'normal':
        logging.info("Publishing new apartment's to normal fanout exchange")
        channel.basic_publish(exchange='agency_normal', routing_key='default',
                              body=json.dumps(apartment_data, indent=2).encode('utf-8'))
        # some waiting logic here...
        logging.info("Publishing new apartment's to site after some time in normal.")
        channel.basic_publish(exchange='agency_site', routing_key='default',
                              body=json.dumps(apartment_data, indent=2).encode('utf-8'))

        channel.close()


if __name__ == "__main__":
    for ap in apartments_tread:
        send_apartment_to_clients(ap)
