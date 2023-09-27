import os
import time
import sys
import argparse

def child():
    print("Hi, I'm the child, PID", os.getpid(), "my parent is", os.getppid())
    time.sleep(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, required=True)
    args = parser.parse_args()
    
    processes = []

    for i in range(args.number):
        childpid = os.fork()
        if childpid == 0:
            child()
            sys.exit(0)
        else:
            processes.append(childpid)

    # Esperar a que todos los procesos hijos terminen
    for pid in processes:
        os.waitpid(pid, 0)

if __name__ == "__main__":
    main()
