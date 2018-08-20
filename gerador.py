
from ambiente_virtual import AmbienteVirtual
from linux import Linux
from windows import Windows
from diretorio import Diretorio


import platform

if __name__ == '__main__':

    tipo_sistema_operacional = eval(platform.system())

    AmbienteVirtual().instalar_virtual_env(tipo_sistema_operacional)

    Diretorio().criar_diretorio('projeto')
