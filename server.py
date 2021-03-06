#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Clase (y programa principal) para un servidor de eco en UDP simple."""

import socketserver
import sys
import json
import time

ATTR_TIME = '%Y-%m-%d %H:%M:%S +0000'


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """Echo server class."""

    Users = {}

    def register2json(self):
        """metodo para registrar usuarios en json."""
        with open('registered.json', 'w') as outfile:
            json.dump(self.Users, outfile, indent=3)

    def check_exp(self, act_time):
        """Checkear expiracion del user."""
        list_del = []
        for address in self.Users:
            if self.Users[address]['expire'] <= act_time:
                list_del.append(address)
        for address in list_del:
            del self.Users[address]

    def json2registered(self):
        """metodo para leer json externo."""
        try:
            with open('registered.json', 'r') as infile:
                self.Users = json.loads(infile)
        except:
            pass

    def handle(self):
        """handle method of the server class."""
        if not self.Users:
            self.json2registered()
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        msg = self.rfile.read().decode('utf-8')
        metodo, address, protocol, expire = msg.split(' ')
        _, address = address.split(':')
        expire, _, _ = expire.split('\r')
        actual_time = time.time()
        exp_time = actual_time + int(expire)
        exp_time = time.strftime(ATTR_TIME, time.gmtime(exp_time))
        self.Users[address] = {'address': self.client_address[0],
                               'expire': exp_time}
        self.register2json()
        self.check_exp(time.strftime(ATTR_TIME, time.gmtime(actual_time)))

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 server.py puerto")
    PORT = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
