#Escribir un programa que en ejecución genere dos procesos, uno padre y otro hijo.
#El hijo debe escribir "Soy el hijo, PID YYYY" 5 veces (YYYY es el pid del hijo).
#El padre debe escribir "Soy el padre, PID XXXX, mi hijo es YYYY" 2 veces (XXXX es el pid del padre).
#El padre debe esperar a que termine el hijo y mostrar el mensaje "Mi proceso hijo, PID YYYY, terminó".
#El hijo al terminar debe mostrar "PID YYYY terminando".

import os
import time
import sys

def child():
    for i in range(5):
        print("Hi, im the child, PID", os.getpid())
        time.sleep(1)
    print("PID", os.getpid(), "done")

def parent():
    for i in range(2):
        print("Hi, im the parent, PID", os.getpid(), "my child is", childpid)
        time.sleep(1)
    os.wait()
    print("My child process, PID", childpid, "has finished")

childpid = os.fork()
if childpid == 0:
    child()
else:
    parent()