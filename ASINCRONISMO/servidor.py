import asyncio
import subprocess
import argparse
import datetime

async def handle_client(client_reader, client_writer, log_file):
    while True:
        command = (await client_reader.read(1024)).decode()
        if not command:
            break

        # Registrar el comando y la fecha/hora en el archivo de registro
        log_entry = f"{datetime.datetime.now()}: {command}\n"
        log_file.write(log_entry)
        log_file.flush()

        try:
            # Ejecutar el comando y capturar la salida estándar y de error
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            client_writer.write(b"OK\n" + result)
            await client_writer.drain()
        except subprocess.CalledProcessError as e:
            client_writer.write(b"ERROR\n" + e.output)
            await client_writer.drain()

async def main():
    parser = argparse.ArgumentParser(description="Servidor para ejecutar comandos remotos.")
    parser.add_argument("-p", "--puerto", type=int, default=9999, help="Puerto para escuchar (predeterminado: 9999)")
    parser.add_argument("-l", "--log_file", help="Archivo de registro de la sesión")
    args = parser.parse_args()

    if args.log_file:
        log_file = open(args.log_file, "a")
    else:
        log_file = None

    server = await asyncio.start_server(
        client_connected_cb=lambda client_reader, client_writer: asyncio.ensure_future(
            handle_client(client_reader, client_writer, log_file)
        ),
        host="0.0.0.0",
        port=args.puerto,
    )

    print(f"Servidor escuchando en el puerto {args.puerto}...")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
