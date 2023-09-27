import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description="Cliente para ejecutar comandos remotos.")
    parser.add_argument("-a", "--ip_servidor", required=True, help="Dirección IP del servidor")
    parser.add_argument("-p", "--puerto", type=int, default=9999, help="Puerto del servidor (predeterminado: 9999)")
    parser.add_argument("-l", "--log_file", help="Archivo para el registro de la sesión")
    args = parser.parse_args()

    if args.log_file:
        log_file = open(args.log_file, "a")
    else:
        log_file = None

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((args.ip_servidor, args.puerto))

    while True:
        command = input("> ")
        if not command:
            break

        client.send(command.encode())

        response = client.recv(4096).decode()
        status, result = response.split("\n", 1)
        print(result)

        if log_file:
            log_file.write(result + "\n")
            log_file.flush()

if __name__ == "__main__":
    main()