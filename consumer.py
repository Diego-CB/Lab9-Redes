from kafka import KafkaConsumer
from coding import *

# Configuración del consumidor
consumer = KafkaConsumer(
    '20807',  # Tema al que suscribirse
    bootstrap_servers='157.245.244.105:9092',  # Servidor Kafka
    group_id='lab9.alumchat.xyz',  # Identificador del grupo de consumidores
    # value_deserializer=lambda value: json.loads(value.decode('utf-8'))  # Deserializador para los valores
)

# Escuchar y procesar mensajes
for message in consumer:
    # El mensaje es un objeto de tipo ConsumerRecord
    # message.value contiene el valor del mensaje (JSON en este caso)
    print('Mensaje Encriptado:', message.value, f'({len(message.value)} bytes)')
    decoded = Decode(message.value)
    print('Mensaje recibido:', decoded)

