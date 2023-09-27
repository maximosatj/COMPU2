import socket
import subprocess
import argparse
import os
import datetime

def handle_client(client_socket, log_file):
    while True:
        command = client_socket.recv(1024).decode()
        if not command:
            break

        # Registrar el comando y la fecha/hora en el archivo de registro
        log_entry = "{}: {}\n".format(datetime.datetime.now(), command)
        log_file.write(log_entry)
        log_file.flush()

        try:
            # Ejecutar el comando y capturar la salida estándar y de error
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            client_socket.send("OK\n".encode() + result)
        except subprocess.CalledProcessError as e:
            client_socket.send("ERROR\n".encode() + e.output)

def main():
    parser = argparse.ArgumentParser(description="Servidor para ejecutar comandos remotos.")
    parser.add_argument("-p", "--puerto", type=int, default=9999, help="Puerto para escuchar (predeterminado: 9999)")
    parser.add_argument("-l", "--log_file", help="Archivo de registro de la sesión")
    args = parser.parse_args()

    if args.log_file:
        log_file = open(args.log_file, "a")
    else:
        log_file = None

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", args.puerto))
    server.listen(5)

    print(f"Servidor escuchando en el puerto {args.puerto}...")

    while True:
        client_socket, addr = server.accept()
        print(f"Conexión aceptada desde {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, log_file))
        client_handler.start()

if __name__ == "__main__":
    main()