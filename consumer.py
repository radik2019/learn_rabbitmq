import pika
from settings import get_connection

def callback(ch, method, properties, body):
    print(f"[{method.exchange}] ({method.routing_key}) -> {body.decode()} "
          f"props: {properties.headers if properties.headers else ''}")


def main():
    connection = get_connection()
    channel = connection.channel()

    # --- 1. Direct exchange ---
    channel.exchange_declare(exchange="direct_logs", exchange_type="direct", durable=True)
    channel.queue_declare(queue="error_queue", durable=True)
    channel.queue_bind(exchange="direct_logs", queue="error_queue", routing_key="error")
    channel.basic_consume(queue="error_queue", on_message_callback=callback, auto_ack=True)

    channel.queue_declare(queue="info_queue", durable=True)
    channel.queue_bind(exchange="direct_logs", queue="info_queue", routing_key="info")
    channel.basic_consume(queue="info_queue", on_message_callback=callback, auto_ack=True)

    # --- 2. Fanout exchange (broadcast) ---
    channel.exchange_declare(exchange="broadcast", exchange_type="fanout", durable=True)

    # consumer 1
    channel.queue_declare(queue="fanout_queue_1", durable=True)
    channel.queue_bind(exchange="broadcast", queue="fanout_queue_1")
    channel.basic_consume(queue="fanout_queue_1", on_message_callback=callback, auto_ack=True)

    # consumer 2
    channel.queue_declare(queue="fanout_queue_2", durable=True)
    channel.queue_bind(exchange="broadcast", queue="fanout_queue_2")
    channel.basic_consume(queue="fanout_queue_2", on_message_callback=callback, auto_ack=True)



    # --- 3. Topic exchange ---
    channel.exchange_declare(exchange="topic_logs", exchange_type="topic", durable=True)

    channel.queue_declare(queue="order_queue", durable=True)
    # channel.queue_bind(exchange="topic_logs", queue="order_queue", routing_key="order.*")
    channel.queue_bind(exchange="topic_logs", queue="order_queue", routing_key="order.complete")
    channel.basic_consume(queue="order_queue", on_message_callback=callback, auto_ack=True)

    channel.queue_declare(queue="shipped_queue", durable=True)
    channel.queue_bind(exchange="topic_logs", queue="shipped_queue", routing_key="order.shipped.italy")
    channel.basic_consume(queue="shipped_queue", on_message_callback=callback, auto_ack=True)

    channel.queue_declare(queue="all_shipped", durable=True)
    channel.queue_bind(exchange="topic_logs", queue="all_shipped", routing_key="order.shipped.#")
    channel.basic_consume(queue="all_shipped", on_message_callback=callback, auto_ack=True)
    


    # --- 4. Headers exchange ---
    channel.exchange_declare(exchange="headers_logs", exchange_type="headers", durable=True)
    channel.queue_declare(queue="pdf_reports", durable=True)
    channel.queue_bind(
        exchange="headers_logs",
        queue="pdf_reports",
        arguments={"x-match": "all", "format": "pdf", "type": "report"}
    )
    channel.basic_consume(queue="pdf_reports", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages from all exchanges. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    main()
