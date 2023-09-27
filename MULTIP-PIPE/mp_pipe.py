import multiprocessing
import os

def proceso_lectura(pipe):
    while True:
        mensaje = input("Escribe un mensaje: ")
        pipe.send(mensaje)

def proceso_muestra(pipe):
    pid = os.getpid()
    while True:
        mensaje = pipe.recv()
        print(f"Leyendo (pid: {pid}): {mensaje}")

if __name__ == "__main__":
    pipe_a, pipe_b = multiprocessing.Pipe()

    proceso1 = multiprocessing.Process(target=proceso_lectura, args=(pipe_a,))
    proceso2 = multiprocessing.Process(target=proceso_muestra, args=(pipe_b,))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()
