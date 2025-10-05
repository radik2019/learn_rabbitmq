import pika
from settings import get_connection
from settings import get_connection


def publish_default(queue_name, message):
    connection = get_connection()
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange="",
        routing_key=queue_name,
        body=message,
        properties=pika.BasicProperties(delivery_mode=2),
    )
    print(f"[default] Sent '{message}' to queue '{queue_name}'")
    connection.close()


def publish_direct(message, routing_key):
    connection = get_connection()
    channel = connection.channel()

    channel.exchange_declare(exchange="direct_logs", exchange_type="direct", durable=True)
    channel.basic_publish(
        exchange="direct_logs",
        routing_key=routing_key,
        body=message,
        properties=pika.BasicProperties(delivery_mode=2),
    )
    print(f"[direct] Sent '{message}' with key '{routing_key}'")
    connection.close()


# --- 3. Fanout exchange ---
def publish_fanout(message):
    connection = get_connection()
    channel = connection.channel()

    channel.exchange_declare(exchange="broadcast", exchange_type="fanout", durable=True)
    channel.basic_publish(exchange="broadcast", routing_key="", body=message)
    print(f"[fanout] Broadcast '{message}'")
    connection.close()


# --- 4. Topic exchange ---
def publish_topic(message, routing_key):
    connection = get_connection()
    channel = connection.channel()

    channel.exchange_declare(exchange="topic_logs", exchange_type="topic", durable=True)
    channel.basic_publish(
        exchange="topic_logs",
        routing_key=routing_key,
        body=message,
        properties=pika.BasicProperties(delivery_mode=2),
    )
    print(f"[topic] Sent '{message}' with key '{routing_key}'")
    connection.close()


# --- 5. Headers exchange ---
def publish_headers(message, headers):
    connection = get_connection()
    channel = connection.channel()

    channel.exchange_declare(exchange="headers_logs", exchange_type="headers", durable=True)
    channel.basic_publish(
        exchange="headers_logs",
        routing_key="",  # non serve
        body=message,
        properties=pika.BasicProperties(headers=headers),
    )
    print(f"[headers] Sent '{message}' with headers {headers}")
    connection.close()


# if __name__ == "__main__":
#     # Default exchange
#     publish_default("task_queue", "Do the laundry")

#     # Direct
#     publish_direct("Errore critico!", "error")
#     publish_direct("Info di sistema", "info")

#     # Fanout
#     publish_fanout("Broadcast: maintenance at midnight")

#     # Topic
    
#     publish_topic("Ordine creato", "order.created")
#     publish_topic("Ordine spedito in Italia", "order.shipped.italy")
#     publish_topic("Ordine annullato", "order.canceled")

#     # Headers
#     publish_headers("Report PDF pronto", {"format": "pdf", "type": "report"})
#     publish_headers("Report Excel pronto", {"format": "xls", "type": "report"})
