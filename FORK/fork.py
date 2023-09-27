import argparse
import os
import multiprocessing


def calcular_suma_pares(pid, verbose=False):
    inicio_msg = f"Starting process {pid}" if verbose else ""
    fin_msg = f"Ending process {pid}" if verbose else ""
    suma_pares = sum(x for x in range(0, pid + 1, 2))

    print(f"{pid} - {os.getppid()}: {suma_pares}")
    
    if verbose:
        print(inicio_msg)
        print(fin_msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calcula la suma de números pares en procesos hijos.")
    parser.add_argument("-n", type=int, required=True, help="Número de procesos hijos a generar.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo verboso.")
    args = parser.parse_args()

    if args.n <= 0:
        print("El número de procesos debe ser mayor que cero.")
        exit(1)

    process_list = []

    for _ in range(args.n):
        p = multiprocessing.Process(target=calcular_suma_pares, args=(os.getpid(), args.verbose))
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()


