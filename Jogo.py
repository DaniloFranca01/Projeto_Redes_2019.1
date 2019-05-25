'''
Created on 22 de mai de 2019

@author: danilo
'''
import time
from Cliente import Client
from Cliente import P2p
from Servidor import Server
from random import randint
from multiprocessing import sys

if __name__ == '__main__':
    while True:
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