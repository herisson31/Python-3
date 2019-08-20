from random import randint
from tkinter import Frame, Label, Button, mainloop

dados = [randint(1, 60), randint(1, 60), randint(1, 60),
         randint(1, 60), randint(1, 60), randint(1, 60)]

print('*' * 40)
print(f'{"MEGA SENA":^40}')
print('*' * 40)
# print(f'Numeros Sorteados: {dados}')



class Application(Frame):
    def __init__(self, msg, master=None):
        Frame.__init__(self, master)

        self.run = None
        self.msg = Label(self, text="Numeros Sorteados")
        self.msg.pack()
        self.frame1 = Frame(msg, pady=12)
        self.frame1.pack()
        self.jogo = Label(self, text=format(dados))
        self.jogo.pack()
        sortear = Button(self.frame1, font=fonte1, text="Sortear", command=self.sortear)
        self.bye.pack()
        self.pack()
        # Botão multiplicar
        #multiplicar = Button(self.frame4, font=fonte1, text='Calcular ICMS', command=self.multiplicar)
        #multiplicar.pack(side=LEFT)

app = Application()
app.master.title("MEGA SENA")
app.master.geometry("200x200+100+100")
mainloop()
