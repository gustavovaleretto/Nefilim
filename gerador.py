from __future__ import absolute_import, unicode_literals

from core.ambiente_virtual import AmbienteVirtual
from core.django import Django
from core.flask import Flask
from core.instala_framework import InstalaFramework
from core.linux import Linux
from core.windows import Windows
from core.diretorio import Diretorio


import platform

if __name__ == '__main__':

    print('Gerador automático de projetos em python....')

    tipo_sistema_operacional = eval(platform.system())

    nome_projeto = input('Informe o nome do projeto:  ')

    framework = input('Informe qual framework deseja utilizar:  ')

    framework = eval(framework)

    AmbienteVirtual().instalar_virtual_env(tipo_sistema_operacional,
                                           nome_projeto)

    InstalaFramework().instalar_framework(framework)

    # Diretorio().criar_diretorio('projeto')
