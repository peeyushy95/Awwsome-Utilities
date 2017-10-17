# Author : megamind0_0

import os,json
from sys import argv
from http.server import BaseHTTPRequestHandler, HTTPServer

class HttpHandler(BaseHTTPRequestHandler):

    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()

    def do_GET(self):
        self.set_headers()
        file = os.path.join(os.path.dirname(__file__), 'data.json')
        f = open(file, 'rb')
        file_data = f.read()
        f.close()
        self.wfile.write(file_data)

    def do_POST(self):
        self.set_headers()
        posData = self.rfile.read(int(self.headers['Content-Length']))
        # Return Post data back
        self.wfile.write(posData)

if __name__ == "__main__":
    port = int(argv[1]) if len(argv) == 2 else 8081
    serverAddress = ('', port)
    httpd = HTTPServer(serverAddress, HttpHandler)
    print('Server Started!!')
    httpd.serve_forever()
