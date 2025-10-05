import pika

from settings import get_connection
from callbacks import *


def main():
    connection = get_connection()

    channel = connection.channel()
    channel.queue_declare(queue="shipped_queue_it", durable=True)
    channel.queue_bind(exchange="topic_logs", queue="shipped_queue_it", routing_key="order.shipped.italy")
    channel.basic_consume(queue="shipped_queue_it", on_message_callback=callback_fr, auto_ack=True)

    print(" [*] italia in attesa di messaggi")
    channel.start_consuming()



main()
