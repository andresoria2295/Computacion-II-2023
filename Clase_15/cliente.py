"""
1 - Cuándo y por qué se produce el error BrokenPipeError: [Errno 32] Broken Pipe ?
"""

#!/usr/bin/python3
import socket
import sys

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
#host = sys.argv[1]

#port = int(sys.argv[2])
port = 50001

print("Conectando...")
# connection to hostname on the port.
s.connect((host, port))
print("Handshake realizado con exito!")

# Receive no more than 1024 bytes
print("Esperando datos desde el server.")
msg = s.recv(1024)
#print (msg.decode('ascii'))
print (msg.decode('utf-8'))
s.close()
print("Cerrando conexión...")

"""
El error "BrokenPipeError: [Errno 32] Broken pipe" ocurre cuando se intenta escribir en un socket
que ha sido cerrado por el otro extremo. Esto sucede cuando el cliente cierra la conexión antes
de que el servidor haya terminado de escribir todos los datos.

Este error se produce porque el servidor intenta escribir en un socket que ya no está disponible
para escribir, lo que resulta en un "pipe roto". El término "pipe roto" se refiere a una situación
en la que el extremo receptor de un flujo de datos ha sido cerrado inesperadamente.
"""
