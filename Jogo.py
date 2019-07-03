'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF975 -- Redes de Computadores

Autor:    Danilo Leite de Franca
Email:    dlf3@cin.ufpe.br
Data:        2019-05-19

Descricao:  Arquivo do jogo, onde é inicializada a parametrização de objetos e gerenciamento de conexões


Licenca: The MIT License (MIT)
            Copyright(c) 2019 Danilo Leite de Franca
'''

import time
from Peer import Peer
from Jogador import Jogador
from random import randint
from Sala import Sala

class P2p:
    '''
    Classe que contém a lista dos peers
    '''
    peers = ['127.0.0.1']

def menu():
    '''
    Função que representa o Menu, onde há a parametrização dos objetos
    '''
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


