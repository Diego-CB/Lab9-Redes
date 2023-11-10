from sensor import generador
from kafka import KafkaProducer
import json
import random
import time
from coding import *

serializer = lambda value: json.dumps(value).encode('utf-8')

producer = KafkaProducer(bootstrap_servers='157.245.244.105:9092')

def produce(time):
    msg = generador()
    print('Mensaje enviado:', msg)
    msg = Encode(msg)
    print('Mensaje encoded:', msg, len(msg), 'bytes')
    future = producer.send('20807', msg)
    result = future.get(timeout=time)
    producer.flush()

if __name__ == '__main__':
    while True:
        rest = random.randint(15, 30)
        produce(rest)
        time.sleep(rest)