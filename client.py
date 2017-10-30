#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Programa cliente UDP que abre un socket a un servidor."""

import socket
import sys

try:
    _, SERVER, PORT, METODO, SIP_ADDRESS, EXPIRES = sys.argv

except IndexError:
    sys.exit('Usage: client.py ip puerto register sip_address expires_value')

PORT = int(PORT)
PROTOCOL = 'SIP/2.0\r\n'
DATA = ' '.join([METODO.upper(), "sip:" + SIP_ADDRESS, PROTOCOL])
DATA = DATA + 'Expires: ' + EXPIRES + '\r\n\r\n'
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", DATA)
    my_socket.send(bytes(DATA, 'utf-8'))
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
print("Socket terminado.")
