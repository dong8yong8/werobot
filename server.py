#coding=utf-8
import itchat, time
import socket
from itchat.content import *

ipPort = ('127.0.0.1', 12345)
s = socket.socket()         # 创建 socket 对象
s.bind(ipPort)
s.listen(5)

while True:
    c, addr = s.accept()
    msg = c.recv(1024)
    s.send(msg)
    print('----------')
    print(msg)


