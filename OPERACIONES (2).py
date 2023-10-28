import threading
import time
from random import random

def imprimir_mensaje(mensaje):
    print(mensaje, end='', flush=True)
    time.sleep(2)  # Pausa de 2 segundos

def ejecutar_con_delay(func, delay, *args, **kwargs):
    time.sleep(delay)
    func(*args, **kwargs)

def resta(a, b, result_dict):
    result = None
    try:
        imprimir_mensaje(f'Comenzando Resta\n')
        result = a - b
        result_dict['resta'] = result
    except Exception as e:
        imprimir_mensaje(f'Error en la resta: {e}\n')
    finally:
        imprimir_mensaje(f'Finalizando Resta: {a} - {b} = {result}\n')

def suma(a, b, result_dict):
    result = None
    try:
        imprimir_mensaje(f'Comenzando Suma\n')
        result = a + b
        result_dict['suma'] = result
    except Exception as e:
        imprimir_mensaje(f'Error en la suma: {e}\n')
    finally:
        imprimir_mensaje(f'Finalizando Suma: {a} + {b} = {result}\n')

def division(a, b, result_dict):
    result = None
    try:
        imprimir_mensaje(f'Comenzando División\n')
        if b != 0:
            result = a / b
            result_dict['division'] = result
        else:
            raise Exception('División por cero no permitida')
    except Exception as e:
        imprimir_mensaje(f'Error en la división: {e}\n')
    finally:
        imprimir_mensaje(f'Finalizando División: {a} / {b} = {result}\n')

def multiplicacion(a, b, result_dict):
    result = None
    try:
        imprimir_mensaje(f'Comenzando Multiplicación\n')
        result = a * b
        result_dict['multiplicacion'] = result
    except Exception as e:
        imprimir_mensaje(f'Error en la multiplicación: {e}\n')
    finally:
        imprimir_mensaje(f'Finalizando Multiplicación: {a} * {b} = {result}\n')

# Ejemplo de uso
a = 10
b = 5

result_dict = {}  # Diccionario para almacenar los resultados de las operaciones
threads = []

# Agregamos las funciones a la lista de hilos con un retraso aleatorio
threads.append(threading.Thread(target=ejecutar_con_delay, args=(resta, random(), a, b, result_dict)))
threads.append(threading.Thread(target=ejecutar_con_delay, args=(suma, random(), a, b, result_dict)))
threads.append(threading.Thread(target=ejecutar_con_delay, args=(division, random(), a, b, result_dict)))
threads.append(threading.Thread(target=ejecutar_con_delay, args=(multiplicacion, random(), a, b, result_dict)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

if len(result_dict) == 4:  # Si se han completado todas las operaciones
    resultado_final = sum(result_dict.values())
    imprimir_mensaje(f'Resultado Final: {resultado_final}\n')
else:
    imprimir_mensaje('Error en una de las operaciones\n')
