#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

PORT = int(sys.argv[1])


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    Users = {}
    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"Hemos recibido tu peticion")
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'), self.client_address)
            _,Line,_  = line.decode('utf-8').split(' ')
            _,address = Line.split(':')
            SIPRegisterHandler.Users[address] = self.client_address[0]
            print(SIPRegisterHandler.Users)

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
