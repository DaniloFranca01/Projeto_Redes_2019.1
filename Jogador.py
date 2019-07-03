'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF975 -- Redes de Computadores

Autor:    Danilo Leite de Franca
Email:    dlf3@cin.ufpe.br
Data:        2019-05-19

Descricao:  Classe Jogador.


Licenca: The MIT License (MIT)
            Copyright(c) 2019 Danilo Leite de Franca
'''

class Jogador(object):
    '''
    Representacao de um jogador
    '''


    def __init__(self, nome):
        self.nome = nome
        self.organizador = False
        self.tipo = ''
