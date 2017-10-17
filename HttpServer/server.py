# Author : megamind0_0

import os,json
from sys import argv
from http.server import BaseHTTPRequestHandler, HTTPServer

JsonContent = 'application/json'
HtmlContent = 'text/html'

InputParamConsidered = False
pathsAllowed = ['/p1']

class HttpHandler(BaseHTTPRequestHandler):

    def set_headers(self,contentType, Resp = 200):
        self.send_response(Resp)
        self.send_header('Content-type',contentType)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        file = os.path.join(os.path.dirname(__file__), 'data.json')
        f = open(file, 'rb')
        file_data = f.read()
        f.close()
        if InputParamConsidered == False :
            self.set_headers(JsonContent)
            self.send_rqst_resp(file_data)
        else:
            self.send_param_based_resp()

    def do_POST(self):
        posData = self.rfile.read(int(self.headers['Content-Length']))
        # Return Post data back
        if InputParamConsidered == False :
            self.set_headers(JsonContent)
            self.send_rqst_resp(posData)
        else:
            self.send_param_based_resp()

    def send_rqst_resp(self,data):
        self.wfile.write(data)

    def send_param_based_resp(self):
        if self.path  ==  pathsAllowed[0]:
            self.set_headers(JsonContent)
            self.send_rqst_resp(json.dumps({"resp" : "p1 was parameter"}).encode())
        else:
            self.set_headers(HtmlContent,404)
            self.send_error(404)

if __name__ == "__main__":
    port = int(argv[1]) if len(argv) == 2 else 8081
    serverAddress = ('', port)
    httpd = HTTPServer(serverAddress, HttpHandler)
    print('Server Started!!')
    httpd.serve_forever()
