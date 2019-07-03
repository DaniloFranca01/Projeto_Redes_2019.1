'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF975 -- Redes de Computadores

Autor:    Danilo Leite de Franca
Email:    dlf3@cin.ufpe.br
Data:        2019-05-19

Descricao:  Classe Sala.


Licenca: The MIT License (MIT)
            Copyright(c) 2019 Danilo Leite de Franca
'''

class Sala(object):
    '''
    Representacao de uma sala de jogo
    '''

    def __init__(self, limite,proprietario):
        self.__limite = limite
        self.__proprietario = proprietario
        self.participantes = []
        self.totalPartcipantes = 0
        self.ranking =[]
        self.status = ""

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def proprietario(self):
        return self.__proprietario

    @proprietario.setter
    def proprietario(self, proprietario):
        self.__proprietario = proprietario

    def addParticipantes(self,participante):
        self.participantes.append(participante)
        self.totalPartcipantes +=1

    def checkSala(self):
        if self.limite < self.totalPartcipantes:
            return False
        elif self.limite == self.totalPartcipantes:
            return True
        else:
            return None


