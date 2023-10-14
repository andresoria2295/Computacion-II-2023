'''
En el ejercicio de la clase 15 se proponía el siguiente ejercicio:
Realizar dos versiones de un servidor de mayúsculas que atienda múltiples clientes
de forma concurrente utilizando multiprocessing y threading utilizando sockets TCP.
1- Actualizar el servidor para que sea un servidor asincrónico.
'''
#!/usr/bin/python3
import asyncio

async def send_message():
    #Establece la conexión con el servidor.
    reader, writer = await asyncio.open_connection('127.0.0.1', 50010)

    try:
        while True:
            #Solicita al usuario que escriba un mensaje.
            message = input("Escribe un mensaje. Si deseas salir, escribe 'exit': ")
            #Codifica el mensaje y lo envía al servidor.
            writer.write(message.encode())
            #Espera hasta que se vacíe el búfer de escritura (para evitar enviar datos incompletos).
            await writer.drain()

            #Si el usuario escribe 'exit', se sale del bucle.
            if message.lower() == 'exit':
                break

            #Lee hasta 100 bytes de datos del servidor.
            data = await reader.read(100)
            #Decodifica los datos en un mensaje y lo imprime.
            response = data.decode()
            print("Respuesta del servidor: {}".format(response))

    finally:
        print("Cerrando la conexión..")
        #Cierra la conexión con el servidor.
        print("Conexión finalizada.")
        writer.close()

        #Espera hasta que la conexión se cierre completamente (opcional).
        #await writer.wait_closed()

async def main():
    #Llama a la función send_message() para interactuar con el servidor.
    await send_message()

if __name__ == '__main__':
    #Configura el bucle de eventos asyncio.
    loop = asyncio.get_event_loop()
    #Ejecuta la función principal (main) y espera hasta que termine.
    loop.run_until_complete(main())
    #Cierra el bucle de eventos.
    loop.close()
