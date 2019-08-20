"""
Calcular ICMS com GUI em Tkinter.

"""

__license__ = 'GPL, GNU Public License'
__author__ = 'Herisson Ricardo'
__credits__ = 'http://doc.async.com.br/python/Tkinter/index.htm'

from tkinter import *
from math import *
from sys import *

class ICMS:
    def __init__(self, toplevel):
        # Janela
        toplevel.title('Calcular ICMS')
        toplevel.geometry("290x260")

        # Espaçamento
        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        # Box 1
        self.frame2 = Frame(toplevel)
        self.frame2.pack()

        # Box 2
        self.frame3 = Frame(toplevel)
        self.frame3.pack()

        # Operações
        self.frame4 = Frame(toplevel, pady=12)
        self.frame4.pack()

        # Resultado
        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        # Botões
        self.frame6 = Frame(toplevel, pady=12)
        self.frame6.pack()

        # Cor e tamanho das letras
        Label(self.frame1, text='', fg='black',
              font=('Verdana', '10'), height=1).pack()
        fonte1 = ('Verdana', '10')

        # Botão multiplicar
        multiplicar = Button(self.frame4, font=fonte1, text='Calcular ICMS', command=self.multiplicar)
        multiplicar.pack(side=LEFT)

        # Botão base de calculo reduzida ICMS
        multiplicarbs = Button(self.frame4, font=fonte1, text='Calcular BS R ICMS', command=self.multiplicarbs)
        multiplicarbs.pack(side=LEFT)

        # Botão Limpar
        limpar = Button(self.frame5, font=fonte1, text='Limpar', command=self.limpar)
        limpar.pack(side=LEFT)

        # Botão Sair
        sair = Button(self.frame6, font=fonte1, text='Sair', command=self.sair)
        sair.pack(side=LEFT)

        # Box 1 para entrada de número
        Label(self.frame2, text='Aliquota ICMS %:', font=fonte1, width=14).pack(side=LEFT)
        self.valor1 = Entry(self.frame2, width=10, font=fonte1)
        self.valor1.focus_force()
        self.valor1.pack(side=LEFT)

        # Box 2 para entrada de número
        Label(self.frame3, text='Valor Nota :', font=fonte1, width=14).pack(side=LEFT)
        self.valor2 = Entry(self.frame3, width=10, font=fonte1)
        self.valor2.pack(side=LEFT)

        # Resultado
        Label(self.frame5, text=' = ', font=fonte1, width=8).pack(side=LEFT)
        self.msg = Label(self.frame5, width=10, font=fonte1)
        self.msg.pack(side=LEFT)


    def multiplicar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1/100 * valor2
        c = float(c)
        self.msg['text'] = '%f' % (c)

    def multiplicarbs(self):
        valor2 = self.valor2.get()
        valor2 = float(valor2)
        bs= valor2 * 20/100
        c = valor2 - bs
        c = float(c)
        self.msg['text'] = 'R$ %f' % (c)


    def limpar(self):
        pass


    def sair(self):
        app.destroy()


app = Tk()
ICMS(app)
app.mainloop()