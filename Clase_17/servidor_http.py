#!/usr/bin/python3
import http.server
import socketserver

PORT = 1111

class handler_manual (http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('REQUEST: ', self.requestline)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'hola mundo GET\n')
    def do_POST(self):
        print('REQUEST: ', self.requestline)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'hola mundo POST\n')

socketserver.TCPServer.allow_reuse_address = True

myhttphandler = handler_manual

httpd = http.server.HTTPServer(('',PORT),myhttphandler)

print('Opening httpd server at port: ',PORT)

httpd.serve_forever()

httpd.shutdown()
