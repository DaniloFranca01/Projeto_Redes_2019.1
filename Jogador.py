'''
Created on 19 de mai de 2019

@author: danilo
'''

class Jogador(object):
    '''
    classdocs
    '''


    def __init__(self, nome):
        self.__nome = nome
        self.organizador = False
        self.tipo = ''
        '''
        Constructor
        '''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nPalavras(self, nome):
        self.__nome = nome
