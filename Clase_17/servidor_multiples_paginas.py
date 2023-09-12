'''
Implementar un servidor http con el módulo http server que sirva diferentes paginas utilizando
como base el código analizado en clase.
Utilizar links para navegar entre las diferentes paginas.
Modos de verificación:
Terminal : curl http://localhost:1111/page1
Chrome: http://localhost:1111/page1
Links http://localhost:1111/page1
'''
import http.server
import socketserver

PORT = 1111

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        #Obtiene la ruta solicitada por el cliente.
        path = self.path

        #Definir un diccionario de rutas a páginas HTML.
        pages = {
            '/page1': '<html><body><h1>Pagina 1</h1></body></html>',
            '/page2': '<html><body><h1>Pagina 2</h1></body></html>',
            '/page3': '<html><body><h1>Pagina 3</h1></body></html>'
        }

        #Verificar si la ruta solicitada está en el diccionario.
        if path in pages:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            #Codificar la cadena como UTF-8.
            self.wfile.write(pages[path].encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(u'Pagina no encontrada'.encode('utf-8'))
            #curl http://localhost:1111/pagina_inexistente

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True

    httpd = socketserver.TCPServer(('0.0.0.0', PORT), MyHandler)

    print('Abriendo servidor HTTP en el puerto:', PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.shutdown()
