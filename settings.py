import pika

def get_connection():
    """Crea connessione a RabbitMQ"""
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host=HOST,
            port=PORT,
            credentials=pika.PlainCredentials(USER, PASSWORD),
        )
    )

HOST = '192.168.2.68'
PORT = 5672
USER = 'guest'
PASSWORD = 'guest'

