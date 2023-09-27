import os
import time

def child():
    for i in range(5):
        print("Soy el hijo, PID", os.getpid())
        time.sleep(1)
    print("PID", os.getpid(), "terminando")

def parent():
    global childpid
    for i in range(2):
        print("Soy el padre, PID", os.getpid(), "mi hijo es", childpid)
        time.sleep(1)
    os.wait()
    print("Mi proceso hijo, PID", childpid, "terminó")

childpid = os.fork()
if childpid == 0:
    child()
else:
    parent()