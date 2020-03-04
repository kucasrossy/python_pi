from tkinter import * 
from calculate import *

class Apllication:
    def __init__(self, master=None):
        self.wid1 = Frame(master)
        self.wid1.pack()
        self.msg = Label(self.wid1,text='Digite o numero de casas de Pi')
        self.msg.pack()
        self.entrada = Entry(self.wid1)
        self.entrada["width"] = 10
        self.entrada.pack()
        self.resp = Label(self.wid1)
        self.resp.pack()
        self.act = Button(self.wid1)
        self.act['text'] = 'Clique aqui'
        self.act.bind("<Button-1>", self.showResp)
        self.act.pack()
    def showResp(self,event):
        num = self.entrada.get()
        self.resp['text'] = get_pi(int(num))