#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex_pack.py
#
#  Copyright 2017 tavares <tavares@tavares-Inspiron-5558>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#
#
from tkinter import *
from platform import python_version


def main(args):

	root = Tk()
    #janela.title('Minha Janela')
	Label(root, text="Texto superior", bg="blue", fg="black").pack()
	Label(root, text="Texto intermediário", bg="yellow", fg="black").pack()
	Label(root, text="Texto inferior", bg="green", fg="white").pack()

	mainloop()


	return 0

if __name__ == '__main__':
    import sys
    print (python_version())   #somente para verificar que estamos no ambiente virtual python 3.5
    sys.exit(main(sys.argv))