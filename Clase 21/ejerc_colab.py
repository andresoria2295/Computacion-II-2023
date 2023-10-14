#!/usr/bin/python3
import asyncio
import random


async def handle_echo(reader, writer):
    movies = [b'The Matrix', b'Alien', b'The Thing', b'The Terminator', b'Predator', b'The Shining', b'The Fly', b'The Matrix Reloaded', b'The Matrix Revolutions', b'The Terminator 2: Judgement Day', b'The Terminator 3: Rise of the Machines', b'The Terminator: Salvation', b'The Terminator: Genisys', b'The Terminator: Dark Fate', b'Aliens', b'Alien 3', b'Alien: Resurrection', b'Alien vs. Predator', b'Aliens vs. Predator: Requiem', b'Predators', b'Prometheus', b'Alien: Covenant', b'The Shining', b'Doctor Sleep', b'The Fly']  # noqa: E501

    movies = [movie + b'\n' for movie in movies]
    size_list = [str(i).encode() for i in range(1, 101)]

    addr = writer.get_extra_info('peername')

    print(f"Received from {addr!r}")

    writer.write(b"Elija una pelicula para descargar: \n")
    await writer.drain()
    writer.writelines(movies)
    await writer.drain()

    movie_index = await reader.read(100)

    writer.write(f"Descargando {movies[int(movie_index)]}...".encode())

    for mb in size_list:
        await asyncio.sleep(random.uniform(0.1, 0.5))
        writer.write(mb)
        await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
