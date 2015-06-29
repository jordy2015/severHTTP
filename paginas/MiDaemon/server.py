#!/usr/bin/python

import os
import sys
import BaseHTTPServer

var = open("/home/jordy/paginas/index.html", "r");
html= var.read()
var.close()

class RequestHandler (BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET (self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(html)
        return

    def _get_status (self):
        return "Hola mundo mi estatus es:\n" \
               "\n" \
               "Load average: %s\n" % \
               ("%01.2f, %01.2f, %01.2f" % \
                           os.getloadavg())            

def main (args):
    httpd = BaseHTTPServer.HTTPServer(('localhost', 2012), RequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
 
