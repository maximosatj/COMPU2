import socket
import sys
import getopt

def main(argv):
    # Opciones por defecto
    puerto = None
    protocolo = None
    archivo = None

    try:
        opts, args = getopt.getopt(argv, "p:t:f:")
    except getopt.GetoptError:
        print("Uso: servidor.py -p <puerto> -t <tcp/udp> -f <archivo>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-p":
            puerto = int(arg)
        elif opt == "-t":
            protocolo = arg
        elif opt == "-f":
            archivo = arg

    if puerto is None or protocolo is None or archivo is None:
        print("Faltan argumentos.")
        print("Uso: servidor.py -p <puerto> -t <tcp/udp> -f <archivo>")
        sys.exit(2)

    try:
        if protocolo == "tcp":
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocolo == "udp":
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print("Protocolo no válido. Debe ser tcp o udp.")
            sys.exit(2)

        server_socket.bind(("0.0.0.0", puerto))
        server_socket.listen(1)

        print(f"Servidor escuchando en el puerto {puerto} ({protocolo})...")

        while True:
            conn, addr = server_socket.accept()
            with open(archivo, "ab") as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            conn.close()

    except KeyboardInterrupt:
        print("\nServidor detenido.")

if __name__ == "__main__":
    main(sys.argv[1:])
