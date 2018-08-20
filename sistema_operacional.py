from abc import ABCMeta, abstractmethod


class SistemaOperacional(metaclass=ABCMeta):

    @abstractmethod
    def instalar_ambiente_virtual(self):
        pass
