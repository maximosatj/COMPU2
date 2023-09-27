#Realice un programa que genere X procesos hijos. Cada proceso al iniciar deberá mostrar:
#“Soy el proceso X, mi padre es Y” N será el PID de cada hijo, y Y el PID del padre.
#La cantidad de procesos hijos X será pasada mediante el argumento "-n" de línea de comandos.

import os
import time
import sys
import argparse

def child():
    print("Hi, im the child, PID", os.getpid(), "my parent is", os.getppid())
    time.sleep(1)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, required=True)
    args=parser.parse_args()
    for i in range(args.number):
        childpid = os.fork()
        if childpid == 0:
            child()
            sys.exit(0)
        else:
            os.wait()

if __name__=="__main__":
    main()
