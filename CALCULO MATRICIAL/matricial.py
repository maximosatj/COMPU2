import argparse
import numpy as np
from celery import Celery
from math import sqrt, log

# Configura Celery
app = Celery('calculo_matriz', broker='redis://localhost:6379/0')

# Define las tareas de Celery
@app.task
def calcular_elemento(funcion_calculo, elemento):
    if funcion_calculo == 'raiz':
        return sqrt(elemento)
    elif funcion_calculo == 'pot':
        return elemento ** elemento
    elif funcion_calculo == 'log':
        return log(elemento)
    else:
        raise ValueError("Función de cálculo no válida")

def main():
    # Configura los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Calcular una matriz usando Celery')
    parser.add_argument('-f', '--archivo', required=True, help='Ruta al archivo de matriz')
    parser.add_argument('-c', '--funcion_calculo', required=True, choices=['raiz', 'pot', 'log'],
                        help='Función de cálculo (raiz, pot, log)')

    args = parser.parse_args()

    # Lee la matriz desde el archivo
    matriz = np.loadtxt(args.archivo, delimiter=', ')

    # Crea una lista de tareas de Celery
    tareas = []
    for fila in matriz:
        for elemento in fila:
            tarea = calcular_elemento.apply_async((args.funcion_calculo, elemento))
            tareas.append(tarea)

    # Espera a que se completen todas las tareas y obtiene los resultados
    resultados = [tarea.get() for tarea in tareas]

    # Reorganiza los resultados en una matriz
    resultados_matriz = np.array(resultados).reshape(matriz.shape)

    # Imprime la matriz resultante
    print(resultados_matriz)

if __name__ == '__main__':
    main()
