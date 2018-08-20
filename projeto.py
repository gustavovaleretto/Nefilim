from abc import ABCMeta, abstractmethod


class Projeto(ABCMeta):

    @abstractmethod
    def criar_projeto(self, nome):
        print('criando projeto ' + nome)
