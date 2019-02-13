#coding=utf-8
import itchat, time
import socket
from itchat.content import *


ipPort = ('127.0.0.1', 12345)
s = socket.socket()
s.connect(ipPort)

c, addr = s.accept()
msg = c.recv(1024)
print(msg)
s.send('socket test')
