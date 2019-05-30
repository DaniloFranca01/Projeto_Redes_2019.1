'''
Created on 29 de mai de 2019

@author: danilo
'''

class Sala(object):
    '''
    classdocs
    '''


    def __init__(self, limite,proprietario):
        self.__limite = limite
        self.__proprietario = proprietario
        self.participantes = []
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
