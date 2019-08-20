#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  megasena.py
#
#  Copyright 2017 Tavares <tavares@tavares-Inspiron-5558>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import tkinter
from tkinter import *


class megaSenaApp_tk(tkinter.Tk):
    # Tkinter.tk é a classe base para a janela padrão. A nossa classe megaSenaApp_tk irá herdar todas as funcionalidades da classe padrão.

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        # no construtor da nossa classe, apenas chamamo o construtor da classe pai, Tkinter.Tk.__init__()).
        self.parent = parent
        # geralmente necessitaremos  de acessar o pai de um objeto. É uma boa técnica  sempre salvar uma referencia ao pai.
        self.initialize()
        # no método initialize criamos os demais objetos que serão apresentados na tela, inicializamos as variáveis globais (irc..),
        # inicializamos o hardware caso necessário, etc..
        self.run()
    def initialize(self):  # no momento ainda não inicializamos nada
        pass

    # este é ponto onde o programa se inicia


# se foi chamado a partir do interpretador python, o _name_  automaticamente será "__main__"
if __name__ == "__main__":
    app = megaSenaApp_tk(None)  # criamos uma aplicação sem enhum pai, pois é a principal.
    app.title('Minha Mega-Sena')  # especificamos o título de nossa aplicação
    app.mainloop()  # o programa entra no loop de espera de eventos (pressionar de menus, botões, etc..)