import multiprocessing
import time

def worker(pid, queue):
    print(f"Proceso {pid}, PID: {multiprocessing.current_process().pid}")
    time.sleep(pid)
    queue.put(multiprocessing.current_process().pid)

if __name__ == "__main__":
    num_procesos = 10
    cola = multiprocessing.Queue()

    procesos = [multiprocessing.Process(target=worker, args=(i, cola)) for i in range(1, num_procesos + 1)]

    for proceso in procesos:
        proceso.start()

    for proceso in procesos:
        proceso.join()

    resultados = []
    while not cola.empty():
        resultados.append(cola.get())

    print("Resultados:")
    for pid in resultados:
        print(pid)
