'''
Created on 22 de mai de 2019

@author: danilo
'''
import time
from Cliente import Client
from Cliente import P2p
from Servidor import Server
from Jogador import Jogador
from random import randint
from multiprocessing import sys
from Sala import Sala

if __name__ == '__main__':
    while True:

        print("Bem vindo ao SE-PA-RAN-DO!!!")
        nome = int(input("Digite seu nome: "))
        jogador = Jogador(nome)
        jogador.tipo = "JOGADOR"

        print("1 - Criar Sala")
        print("2 - Entrar numa sala")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            limite = int(input("Informe o limite máximo da sala(Não informe para sem limites): "))

            sala = Sala(limite,nome)

        try:
            print("Trying to connect...")
            time.sleep(randint(1,5))
            for peer in P2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass

                if randint(1,10) == 1:
                    try:
                        server = Server()
                    except KeyboardInterrupt:
                        sys.exit(0)
                    except:
                        print("Couldn't start the server...")

        except KeyboardInterrupt:
            sys.exit(0)

