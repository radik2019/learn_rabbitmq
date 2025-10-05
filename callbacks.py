def callback(ch, method, properties, body):
    print(f"[{method.exchange}] ({method.routing_key}) -> {body.decode()} "
          f"props: {properties.headers if properties.headers else ''}")
    
def callback_it(ch, method, properties, body):
    print("+++++  Italy  ++++++")
    print(f"[{method.exchange}] ({method.routing_key}) -> {body.decode()} "
        f"props: {properties.headers if properties.headers else ''}")
    print("\n")


def callback_fr(ch, method, properties, body):
    print("+++++  France  ++++++")
    print(f"[{method.exchange}] ({method.routing_key}) -> {body.decode()} "
        f"props: {properties.headers if properties.headers else ''}")
    print("\n")



def callback_common(ch, method, properties, body):
    print("+++++  Common  ++++++")
    print(f"[{method.exchange}] ({method.routing_key}) -> {body.decode()} "
        f"props: {properties.headers if properties.headers else ''}")
    print("\n")