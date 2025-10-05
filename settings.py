import pika
import os

ITALY_IN_COMMON_CONSUMER = 'ITALY_IN_COMMON_CONSUMER'
FRANCE_IN_COMMON_CONSUMER = 'FRANCE_IN_COMMON_CONSUMER'
RABBITMQ_HOST = 'RABBITMQ_HOST'
FALSE_ENV = ['true', '1']
TRUE_ENV = ['false', '0']

def bool_env(val):
    if isinstance(val, str):
        if val.isdigit():
            return bool(int(val))
        if val.lower() in FALSE_ENV:
            return False
        if val.lower() in TRUE_ENV:
            return True
        return False
    return False

RABBITMQ_HOST = os.getenv(RABBITMQ_HOST, '0.0.0.0')
PORT = 5672
USER = 'guest'
PASSWORD = 'guest'

FRANCE_IN_COMMON_CONSUMER = bool_env(os.getenv(FRANCE_IN_COMMON_CONSUMER, 'True'))
ITALY_IN_COMMON_CONSUMER = bool_env(os.getenv(ITALY_IN_COMMON_CONSUMER, 'True'))

os.getenv('')

def get_connection():
    """Crea connessione a RabbitMQ"""
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=PORT,
            credentials=pika.PlainCredentials(USER, PASSWORD),
        )
    )
