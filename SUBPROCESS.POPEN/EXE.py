import argparse
import subprocess
import os
import datetime

def main():
    # Configuración de los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Ejecuta un comando y guarda su salida en un archivo.")
    parser.add_argument("-c", "--command", required=True, help="El comando a ejecutar")
    parser.add_argument("-f", "--output_file", required=True, help="El archivo para guardar la salida del comando")
    parser.add_argument("-l", "--log_file", required=True, help="El archivo de registro")
    args = parser.parse_args()

    # Comprobar si los archivos de salida y registro existen
    if not os.path.isfile(args.output_file):
        open(args.output_file, "a").close()

    if not os.path.isfile(args.log_file):
        open(args.log_file, "a").close()

    try:
        # Ejecutar el comando y capturar la salida
        process = subprocess.Popen(args.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode == 0:
            with open(args.log_file, "a") as log_file:
                log_file.write("{}: Comando \"{}\" ejecutado correctamente.\n".format(datetime.datetime.now(), args.command))
        else:
            with open(args.log_file, "a") as log_file:
                log_file.write("{}: {}\n".format(datetime.datetime.now(), error.decode().strip()))

        with open(args.output_file, "ab") as output_file:
            output_file.write(output)

    except Exception as e:
        with open(args.log_file, "a") as log_file:
            log_file.write("{}: {}\n".format(datetime.datetime.now(), str(e)))

if __name__ == "__main__":
    main()
