import argparse
import socket

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--puerto", type=int, required=True, help="Puerto en el cual debe atender el servicio")
    args = parser.parse_args()

    host = "0.0.0.0"  # Escucha en todas las interfaces
    puerto = args.puerto

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((host, puerto))
        servidor.listen()
        print(f"Esperando conexiones en el puerto {puerto}...")

        conn, addr = servidor.accept()

        with conn:
            print(f"Conexión establecida desde {addr}")
            while True:
                datos = conn.recv(1024)
                if not datos:
                    break
                texto = datos.decode()
                texto_mayusculas = texto.upper()
                conn.send(texto_mayusculas.encode())
                break  # Solo procesa un fragmento de texto

if __name__ == "__main__":
    main()
