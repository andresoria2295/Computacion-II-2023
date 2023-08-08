#!/usr/bin/python3

import socket

HOST = ''       # Symbolic name meaning all available interfaces
PORT = 50007    # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Waiting for connections...")

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
            print('Connection closed')
