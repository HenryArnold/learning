#!/usr/bin/env python

from socket import *

HOST = '192.168.112.130'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input(">")
    if not data:
        break
    data = bytes(data.encode('utf-8'))
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print (data)

tcpCliSock.close()
