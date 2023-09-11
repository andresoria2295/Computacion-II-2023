#!/usr/bin/python3
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
'''
with socketserver.TCPServer(('',PORT), Handler) as httpd:
    print('serving at port', PORT)
    httpd.serve_forever()
'''

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()
