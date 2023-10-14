'''
En el ejercicio de la clase 15 se proponía el siguiente ejercicio:
Realizar dos versiones de un servidor de mayúsculas que atienda múltiples clientes
de forma concurrente utilizando multiprocessing y threading utilizando sockets TCP.
1- Actualizar el servidor para que sea un servidor asincrónico.
'''
#!/usr/bin/python3
import asyncio

#Función que maneja la comunicación con el cliente.
async def handle_client(reader, writer):
    #Obtiene la dirección del cliente.
    addr = writer.get_extra_info('peername')
    #Muestra un mensaje para indicar que se ha establecido la conexión con el cliente.
    print("Conexión establecida con {0}".format(addr))

    try:
        while True:
            #Lee los datos del cliente (hasta 100 bytes).
            data = await reader.read(100)
            if not data:
                break

            #Decodifica los datos recibidos y elimina espacios en blanco.
            message = data.decode().strip()
            #Muestra el mensaje recibido y la dirección del cliente.
            print("Recibiendo mensaje: '{0}' de {1}..".format(message, addr))

            if message == "exit":
                #Si el cliente envía "exit", se cierra la conexión.
                print("Cerrando conexión con {0}..".format(addr))
                writer.write("Conexión cerrada.".encode('utf-8'))
                #Espera hasta que sea seguro continuar escribiendo en el flujo de datos.
                await writer.drain()
                writer.close()
                #Espera hasta que  writer haya sido cerrado y que todos los recursos asociados con la conexión hayan sido liberados.
                #await writer.wait_closed()
                #Salir del bucle y manejar la desconexión
                break

            #Si no se recibe "exit", se convierte el mensaje a mayúsculas y se envía de vuelta al cliente.
            response = message.upper()
            writer.write(response.encode('utf-8'))
            await writer.drain()

    except ConnectionResetError:
        print("Cierre inesperado de cliente {}".format(addr))

#Función para ejecutar el servidor.
def main():
    #Obtiene el bucle de eventos (event loop) de asyncio.
    loop = asyncio.get_event_loop()
    #Inicia el servidor en la dirección '0.0.0.0' y puerto 50010.
    server = loop.run_until_complete(asyncio.start_server(handle_client, '0.0.0.0', 50010))

    #Muestra un mensaje para indicar que el servidor está en ejecución.
    print("Servidor corriendo..")

    try:
        #Ejecuta el bucle de eventos de asyncio para mantener el servidor en funcionamiento.
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    #Cuando se interrumpe el servidor se cierra el servidor de manera ordenada.
    server.close()
    loop.run_until_complete(server.wait_closed())

if __name__ == '__main__':
    main()
