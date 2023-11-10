

def encode_temp(temp: float) -> int:
    encoded = 0
    number = 0.00

    while number < temp:
        encoded += 1
        number = round(number + 0.01, 2)

    return encoded

def decode_temp(encoded: int) -> float:
    number = 0.00

    for _ in range(encoded):
        number += 0.01

    number = round(number, 2)
    return number


direcciones_viento: list[str] = [ 'N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE' ]

def encode_viento(string:str) -> int:
    if string not in direcciones_viento:
        raise Exception('Direccino de viento invalida para encoding')

    return direcciones_viento.index(string)

def decode_viento(encoded_viento: int) -> str:
    if encoded_viento >= len(direcciones_viento):
        raise Exception('Direccino de viento invalida para decoding')

    return direcciones_viento[encoded_viento]

# json - bytes

import json
import struct

# Función para codificar un objeto JSON en bytes
def Encode(json_data):

    # Codificar dirección del viento como un valor categórico de 3 bits
    viento = bin(encode_viento(json_data['direccion_viento']))[2:]
    add = '' if len(viento) == 3 else ('0' * (3 - len(viento)))
    viento = add + viento
    
    # Codificar humedad como un entero de 1 byte (0-100)
    humedad = bin(json_data['humedad'])[2:]
    add = '' if len(humedad) == 7 else ('0' * (7 - len(humedad)))
    humedad = add + humedad

    # Codificar temperatura como un entero de 2 bytes (puedes ajustar la precisión)
    temp = bin(encode_temp(json_data['temperatura']))[2:]
    add = '' if len(temp) == 14 else ('0' * (14 - len(temp)))
    temp = add + temp


    encoded_data = viento + humedad + temp
    encoded_data = int(encoded_data, 2).to_bytes((len(encoded_data) + 7) // 8, byteorder='big')

    return bytes(encoded_data)
    
# Función para decodificar bytes en un objeto JSON
def Decode(encoded_bytes):
    cadena_bits = ''.join(format(byte, '08b') for byte in encoded_bytes)

    viento = cadena_bits[0:3]
    viento = int(viento, 2)
    viento = decode_viento(viento)

    humedad = cadena_bits[3:10]
    humedad = int(humedad, 2)

    temp = cadena_bits[10:]
    temp = int(temp, 2)
    temp = decode_temp(temp)

    return {
        'direccion_viento': viento,
        'temperatura': temp,
        'humedad': humedad
    }



if __name__ == '__main__':

    print('---- Prueba Temperatura ----')
    og = 50.5
    encoded = encode_temp(og)
    decoded = decode_temp(encoded)
    print('> og', og)
    print('> encoded', encoded)
    print('> decoded', decoded)

    print('---- Prueba viento ----')
    og = 'N'
    encoded = encode_viento(og)
    decoded = decode_viento(encoded)
    print('> og', og)
    print('> encoded', encoded)
    print('> decoded', decoded)

