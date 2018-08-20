import sys
from sistema_operacional import SistemaOperacional


class AmbienteVirtual(object):

    def instalar_virtual_env(self, sistema_operacional):
        sistema_operacional().instalar_ambiente_virtual()
