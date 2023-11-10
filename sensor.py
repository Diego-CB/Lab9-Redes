import random
import numpy as np
import json
from coding import *

direcciones_viento = [ 'N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE' ]

def _gen_temperatura():
    # Parámetros de la distribución uniforme para la temperatura
    media_temperatura = 50  # Media de la distribución de temperatura
    varianza_temperatura = 20  # Varianza de la distribución de temperatura
    # Generar temperatura aleatoria usando distribución uniforme
    temperatura = np.random.uniform(low=media_temperatura - np.sqrt(3*varianza_temperatura), high=media_temperatura + np.sqrt(3*varianza_temperatura))
    # Asegurarse de que la temperatura esté dentro del rango [0, 100]
    temperatura = round(max(0, min(100, temperatura)), 2)
    # print(f'Temperatura generada: {temperatura:.2f}')
    return temperatura


def _gen_humedad():
    # Parámetros de la distribución uniforme para la temperatura
    media_humedad = 50  # Media de la distribución de temperatura
    varianza_humedad = 20  # Varianza de la distribución de temperatura
    # Generar temperatura aleatoria usando distribución uniforme
    humedad = np.random.uniform(low=media_humedad - np.sqrt(3*varianza_humedad), high=media_humedad + np.sqrt(3*varianza_humedad))
    # Asegurarse de que la temperatura esté dentro del rango [0, 100]
    humedad = int(max(0, min(100, humedad)))
    # print(f'Temperatura generada: {temperatura:.2f}')
    return humedad

def _gen_viento():
    ''' Genera direccion de viento random '''
    index = random.randint(0, len(direcciones_viento) - 1)
    return direcciones_viento[index]

def generador():
    return {
        'direccion_viento': _gen_viento(),
        'temperatura': _gen_temperatura(),
        'humedad': _gen_humedad()
    }

if __name__ == '__main__':
    response = generador()
    print(response)
