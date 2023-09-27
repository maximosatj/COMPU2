import os
import signal
import multiprocessing

def handler_A(_signum, _frame):
    pass  # Manejo de la señal USR1 enviada por B a A

def handler_B(_signum, _frame):
    global pipe_bc
    # Proceso B recibe la señal USR1 de A y escribe en el pipe
    mensaje = f"Mensaje 1 (PID={os.getpid()})\n"
    pipe_bc.send(mensaje)
    # Proceso B envía la señal USR1 a C
    os.kill(pid_c, signal.SIGUSR1)

def handler_C(_signum, _frame):
    global pipe_bc, pipe_ac
    # Proceso C recibe la señal USR1 de B y escribe en el pipe
    mensaje = f"Mensaje 2 (PID={os.getpid()})\n"
    pipe_bc.send(mensaje)
    # Proceso C envía la señal USR2 a A
    os.kill(pid_a, signal.SIGUSR2)

if __name__ == "__main__":
    pipe_ab, pipe_bc = multiprocessing.Pipe()
    pipe_ac = multiprocessing.Pipe()

    pid_a = os.getpid()
    pid_b = os.fork()

    if pid_b == 0:  # Proceso B
        signal.signal(signal.SIGUSR1, handler_B)
        pid_c = os.fork()
        if pid_c == 0:  # Proceso C
            signal.signal(signal.SIGUSR1, handler_C)
            while True:
                signal.pause()
        else:
            while True:
                signal.pause()
    else:  # Proceso A
        signal.signal(signal.SIGUSR1, handler_A)
        signal.signal(signal.SIGUSR2, handler_A)
        os.kill(pid_b, signal.SIGUSR1)  # Inicia el proceso enviando la señal USR1 a B

        while True:
            signal.pause()
            mensaje = pipe_bc.recv()
            pipe_ac.send(mensaje)
            signal.pause()
            mensaje = pipe_ac.recv()
            print(f"A (PID={os.getpid()}) leyendo:")
            print(mensaje)
