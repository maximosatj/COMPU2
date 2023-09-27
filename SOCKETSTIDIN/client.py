import socket
import sys
import getopt

def main(argv):
    # Opciones por defecto
    servidor_ip = None
    puerto = None
    protocolo = None

    try:
        opts, args = getopt.getopt(argv, "a:p:t:")
    except getopt.GetoptError:
        print("Uso: cliente.py -a <ip_servidor> -p <puerto> -t <tcp/udp>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-a":
            servidor_ip = arg
        elif opt == "-p":
            puerto = int(arg)
        elif opt == "-t":
            protocolo = arg

    if servidor_ip is None or puerto is None or protocolo is None:
        print("Faltan argumentos.")
        print("Uso: cliente.py -a <ip_servidor> -p <puerto> -t <tcp/udp>")
        sys.exit(2)

    try:
        if protocolo == "tcp":
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocolo == "udp":
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print("Protocolo no válido. Debe ser tcp o udp.")
            sys.exit(2)

        client_socket.connect((servidor_ip, puerto))

        print("Cliente conectado al servidor.")
        print("Ingrese texto (Ctrl+d para terminar):")

        while True:
            try:
                linea = input()
                client_socket.send(linea.encode())
            except EOFError:
                break

    except KeyboardInterrupt:
        print("\nCliente detenido.")

if __name__ == "__main__":
    main(sys.argv[1:])
