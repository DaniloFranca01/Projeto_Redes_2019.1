'''
Created on 22 de mai de 2019

@author: danilo
'''
import time
from Peer import Peer
from Jogador import Jogador
from random import randint
from Sala import Sala

class P2p:
    peers = ['127.0.0.1']

def menu():
    print("Bem vindo ao SE-PA-RAN-DO!!!")
    nome = input("Digite seu nome: ")
    jogador = Jogador(nome)
    jogador.tipo = "JOGADOR"

    print("1 - Criar Sala")
    print("2 - Entrar na sala")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        limite = int(input("Informe o limite máximo da sala(Não informe para sem limites): "))
        sala = Sala(limite,nome)
        sala.addParticipantes(nome)
    elif opcao == 2:
        sala = None

    ret =[jogador,sala,opcao]
    return ret

ret = menu()
while True:
    print("Tentando conectar...")
    time.sleep(randint(1,3))
    for peer in P2p.peers:
        try:
            cliente = Peer(peer,ret[0],2,ret[1])
        except:
            pass
        if randint(1,3) == 1:
            try:
                server = Peer(None,ret[0],1,ret[1])
            except:
                print("Não foi possivel iniciar o servidor")


