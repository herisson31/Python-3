import sys
from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar

class Gui:

    def __init__(self):
        self.Window = Tk()
        self.Window.geometry('{0}x{1}'.format(400, 200))

        self.progress = StringVar()
        self.progress.set(0)
        self.progressBar = Progressbar(self.Window, maximum=100, orient=HORIZONTAL, variable=self.progress)
        self.progressBar.grid(row=10, column=300, sticky=W + E)

        self.startButton = Button(self.Window, text='Iniciar', command=self.start)
        self.startButton.grid(row=10, column=80)
        self.progress_count = 0
    def start(self):
        self.progress.set(self.progress_count)
        self.progress_count += 1
        if self.progress_count < 100:
            self.Window.after(100, self.start)

    def run(self):
        self.Window.mainloop()
        return 0

if __name__ == '__main__':
    Gui = Gui()
    sys.exit(Gui.run())