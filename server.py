#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json

PORT = int(sys.argv[1])


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    Users = {}

    def register2json(self):
        """metodo para registrar usuarios en json"""
        with open(registerde_json, 'w') as outfile:
            json.dump(self.Users, outfile, indent=3)



    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"Hemos recibido tu peticion")
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        msg = self.rfile.read().decode('utf-8')
        print(msg, self.client_address)

if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    #En caso de no llegar register devuelvo 400
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
