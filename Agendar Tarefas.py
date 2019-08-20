import schedule
import time


'''def job():
    print("Hello World")

def hour():
    print(time.strftime("%H:%M:%S", time.time()))

#schedule.every(15).seconds.do(job)
schedule.every(1).days.at("14:55").do(hour)

while True:
    schedule.run_pending()
    time.sleep(1)'''

# Segunda função de agendar tarefas

'''def job():
    print('I am working...')

schedule.every(15).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("15:16").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)'''

# Terceira função de agendar tarefas

'''from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=15, minute=26, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print('hello world')
    
    #...
while True:
    t = Timer(secs, hello_world)
    t.start()'''

# Quarta função de agendar tarefas não funcionou

'''from datetime import date
from apscheduler.schedulers import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

# Define the function that is to be executed
def my_job(text):
    print('text')

# The job will be executed on November 6th, 2009
exec_date = date(2019, 4, 25)

# Store the job in a variable in case we want to cancel it
job = sched.add_date_job(my_job, exec_date, ['text'])

# The job will be executed on November 6th, 2009 at 16:30:05
job = sched.add_date_job(my_job, datetime(2019, 4, 25, 15, 31, 5), ['text'])'''

# Sexta função pra agendar tarefas

from tkinter import *
import pyautogui
import time

class ForceBrute:
    def __init__(self,master=None):
#faz com que a janela não possa ser redimensionada pelo usuario
        master.resizable(width=False,height=False)

#Containers para os itens da interface
        self.con1 = Frame(master)
        self.con1['pady'] = 8
        self.con1.pack()

        self.con2 = Frame(master)
        self.con2['pady'] = 15
        self.con2.pack()


        self.con3 = Frame(master)
        self.con3['pady'] = 30
        self.con3.pack()


        self.con4 = Frame(master)
        self.con4['pady'] = 10
        self.con4.pack()


#itens da interface
        self.tTitle = Label(self.con1)
        self.tTitle['font'] = ('Roboto','30')
        self.tTitle['text'] = 'SiriusForce'
        self.tTitle.pack()

#recebe o valor de aparti de quando deve iniciar
        self.eDe = Entry(self.con2,justify = 'center',relief=RIDGE,width=3)
        self.eDe['font'] = ('Roboto', '20')
        self.eDe.pack(side=LEFT)
#coloca 100 no campo como padrão
        self.eDe.insert(0,'100')

        self.tAte = Label(self.con2)
        self.tAte['font'] = ('Roboto', '20')
        self.tAte['text'] = 'Ate:'
        self.tAte.pack(side=LEFT)

#recebe ate que valor deve ir
        self.eAte = Entry(self.con2,justify = 'center',relief=RIDGE,width=3)
        self.eAte['font'] = ('Roboto', '20')
        self.eAte.pack(side=LEFT)
        self.eAte.insert(0,'999')

#botão para iniciar
        self.bIniciar = Button(self.con3,relief=RIDGE,fg='blue')
        self.bIniciar['font'] =('Roboto', '25')
        self.bIniciar['text'] = 'Iniciar'
        self.bIniciar['command'] = self.iniciar
        self.bIniciar.pack(side=LEFT)


        self.bPausar = Button(self.con3,relief=RIDGE,fg='red')
        self.bPausar['font'] =('Roboto', '25')
        self.bPausar['text'] = 'Pausar'
#      self.bPausar['command'] =           seria para pausar o 'laço'
        self.bPausar.pack(side=LEFT)


#exibe em que numero parou
        self.eCont = Entry(self.con4,justify= 'center',relief=RIDGE,width=3,bg='black',fg='green')
        self.eCont['font'] = ('Roboto', '30')
        self.eCont.pack()




        self.cod = 0


    def iniciar(self):
        self.de = int(self.eDe.get()) -1
        self.ate = int(self.eAte.get())

        print('Iniciado De:',self.de,'Ate:',self.ate) # só para visualizar

        self.cod = self.de

        while(self.cod < self.ate):

            self.cod +=1

            pyautogui.doubleClick(697,363)
            pyautogui.typewrite(str(self.cod))

            print(self.cod)

            self.eCont.delete(0,END)
            self.eCont.insert(0,self.cod)

            pyautogui.click(880,516)

            time.sleep(1.5)


root = Tk()
root.geometry('220x350+400+100')
root.title('Generico')
root.attributes('-topmost',True)
ForceBrute(root)
root.mainloop()