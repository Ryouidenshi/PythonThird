import os
import pika


def send_massage_to_queue(message: str):
    connection = pika.BlockingConnection(pika.URLParameters("amqp://admin:admin123@rabbit:5672/%2F"))
    channel = connection.channel()
    channel.basic_publish(exchange='', routing_key="links", body=message.encode('utf-8'))
    channel.close()
    connection.close()
