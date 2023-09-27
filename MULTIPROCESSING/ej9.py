import os
import sys
import multiprocessing

def first(conn,msg):
        to_send= msg
        conn.send(to_send)
        conn.close()
    
def out(conn):
    pid= os.getpid()
    while True:
            message=(conn.recv())
            print("reading (PID={pid}): {message}".format(pid=pid, message=message))

if __name__ == "__main__":
    msg=input("Ingrese un mensaje: ")
    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=first, args=(child_conn, msg))
    p2 = multiprocessing.Process(target=out, args=(parent_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    sys.exit(0)

