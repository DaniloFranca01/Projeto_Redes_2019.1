'''
Created on 21 de mai de 2019

@author: danilo
'''

import socket
import threading

class Peer(object):

    connections = []
    peers = []

    def __init__(self,adress,jogador,opcao,sala):
        self.cliId = jogador.nome
        self.adress = adress
        self.criaSocket()
        self.sala = sala
        self.pararThread = False
        if opcao == 1 :
            self.sock.bind(('0.0.0.0',10000))
            self.sock.listen(1)
            print("Servidor rodando...")
            iThread = threading.Thread(target=self.sendMsg, args=(self.cliId,))
            iThread.daemon = True
            iThread.start()

            while True:
                c, a = self.sock.accept()
                cThread = threading.Thread(target=self.handler, args= (c, a))
                cThread.daemon = True
                cThread.start()

                self.connections.append(c)
                self.peers.append(a[0])
                print(str(a[0])+ ':' + str(a[1]), "conectado")
                self.sendPeers()

        else:
            self.connectPeer()

            icThread = threading.Thread(target=self.sendMsgCli, args=(self.cliId,))
            icThread.daemon = True
            icThread.start()

            msg= "--new"+self.cliId
            self.sock.send(bytes(msg,'utf-8'))

            while True:
                try:
                    data = self.sock.recv(1024)
                except:
                    break

                dataS = str(data)
                if dataS[2:8] == "--mute":
                    self.pararThread = True
                elif data[0:1] == b'\x11':
                    self.updatePeers(data[1:])
                else:
                    print(str(data,'utf-8'))

    def handler(self, c, a):
        while True:
            try:
                data = c.recv(1024)
                dataS = str(data)
                if dataS[2:7] == "--new":
                    self.sala.addParticipantes(dataS[7:(len(dataS)-1)])
                    ret = self.sala.checkSala()
                    if ret == True:
                        self.sendMsgSys("Jogo Iniciado!")
                    elif ret == False:
                        msg = bytes("--mute",'utf-8')
                        c.send(msg)
                        msg2= bytes("Limite de jogador atingido, entrando como espectador",'utf-8')
                        c.send(msg2)
                else:
                    print(str(data,'utf-8'))
                    for connection in self.connections:
                        connection.send(data)
            except:
                print(str(a[0])+ ':' + str(a[1]), "desconectado")
                self.connections.remove(c)
                self.peers.remove(a[0])
                c.close()
                self.sendPeers()
                break

    def updatePeers(self, peerData):
        self.peers = str(peerData, 'utf-8').split(",")[:-1]

    def sendPeers(self):
        p = ""
        for peer in self.peers:
            p = p + peer  + ","

        for connection in self.connections:
            connection.send(b'\x11'+ bytes(p, "utf-8"))

    def sendMsgSys(self,msg):
        dados = bytes(msg,'utf-8')
        for connection in self.connections:
            connection.send(dados)

    def sendMsg(self,UsrName):
        while True:
            dados = bytes(UsrName+": "+input(""),'utf-8')
            for connection in self.connections:
                connection.send(dados)

    def sendMsgCli(self,UsrName):
        while True:
            try:
                msg = bytes(UsrName+": "+input(""),'utf-8')
                self.sock.send(msg)
            except:
                self.sock.close()
                if self.pararThread == True:
                    for peer in self.peers:
                        self.criaSocket()
                        addr = (peer,10000)
                        self.sock.connect(addr)
                        try:
                            self.sock.send(msg)
                        except:
                            next
                else:
                    break


    def connectPeer(self):
        self.sock.connect((self.adress,10000))


    def criaSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
