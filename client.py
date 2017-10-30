#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
try:
    _, SERVER, PORT, METODO, SIP_ADDRESS, EXPIRES = sys.argv

except IndexError:
    sys.exit('Usage: client.py ip puerto register sip_address expires_value')

PORT = int(PORT)
METODO = METODO.upper()
ADDRESS = "sip:" + SIP_ADDRESS
PROTOCOL = 'SIP/2.0\r\n'
EXPIRES = 'Expires: ' + EXPIRES + '\r\n\r\n'
DATA = ' '.join([METODO,ADDRESS,PROTOCOL])
DATA = DATA + EXPIRES
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", DATA)
    my_socket.send(bytes(DATA, 'utf-8'))
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
