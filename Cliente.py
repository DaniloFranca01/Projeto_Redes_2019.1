'''
Created on 21 de mai de 2019

@author: danilo
'''
import socket
import threading

class P2p:
    peers = ['127.0.0.1']

class Client(object):

    def __init__(self, adress):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((adress,10000))

        iThread = threading.Thread(target=self.sendMsg, args=(sock,))
        iThread.daemon = True
        iThread.start()

        while True:
            try:
                data = sock.recv(1024)
            except:
                break

            if data[0:1] == b'\x11':
                self.updatePeers(data[1:])
            else:
                print(str(data,'utf-8'))

    def updatePeers(self, peerData):
        P2p.peers = str(peerData, 'utf-8').split(",")[:-1]

    def sendMsg(self,sock):
        while True:
            sock.send(bytes(input(""),'utf-8'))
