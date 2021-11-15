#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

hostName = "0.0.0.0"
serverPort = 8080
date = datetime.datetime.now()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Simple-dimple</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Was deployed on: %s</p>" % date, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")