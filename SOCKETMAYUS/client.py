import argparse
import socket

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--direccion_ip", required=True, help="Dirección IP del servidor")
    parser.add_argument("-p", "--puerto", type=int, required=True, help="Puerto del servidor")
    args = parser.parse_args()

    host = args.direccion_ip
    puerto = args.puerto

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((host, puerto))
        texto = input("Introduzca una cadena de texto: ")
        cliente.send(texto.encode())
        datos = cliente.recv(1024)
        texto_mayusculas = datos.decode()
        print("Texto en mayúsculas recibido del servidor:", texto_mayusculas)

if __name__ == "__main__":
    main()
