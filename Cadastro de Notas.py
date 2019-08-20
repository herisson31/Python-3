from tkinter import *

##Definindo a funçãos que salva os dados em um aquivo##

def SalvarDados():
    arq = open("Notas.txt","w")
    arq.write("Diciplina: %s \n"%(diciplina.get()))
    arq.write("Nota: %s \n"%(nota.get()))
    arq.write("Verificação: %s \n"%(verificacao.get()))
    print('Dados armazenados com sucesso !!')

root = Tk()

##Definindo botões e seus titulos##

titulo = StringVar()
Label(root, textvariable = titulo, font = ("Helvetica",15)).pack()
titulo.set("Sistema de Cadastro de Notas")

Label(root, text = "Diciplina", font = ("Helvetica",15)).pack()
diciplina = Entry(root)
diciplina.pack()

Label(root, text = "Nota", font = ("Helvetica",15)).pack()
nota = Entry(root)
nota.pack()

Label(root, text = "Verificação", font = ("Helvetica",15)).pack()
verificacao = Entry(root)
verificacao.pack()

salvar = Button(root, text = "Salvar", command = SalvarDados)
salvar.pack()

mainloop()