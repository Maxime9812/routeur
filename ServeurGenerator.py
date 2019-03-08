from Routeur import Routeur
import os
import shutil
from tkinter import *
from functools import partial
import os, sys
from Shemas import *
from Reseau import *

fileDirectory = "/Users/" + os.getlogin() + "/Desktop/Routeur/"

routeurs = []
reseaux = []
def createFolder():
    if os.path.exists(fileDirectory) != True:
        os.mkdir(fileDirectory)
    else:
        resetRouterFolder()
def resetRouterFolder():
    if os.path.exists(fileDirectory) == True:
        shutil.rmtree(fileDirectory)
        os.mkdir(fileDirectory)

createFolder()

fenetre = Tk()

path = "/Users/" + os.getlogin() + "/Desktop/images"
dirs = os.listdir( path )


fenetre.geometry("400x20")
fenetre.resizable(width=False, height=False)

def start(nbRouteur,shema,ip):
    imageBackground(nbRouteur)
    i = 0
    while i < len(ip):
        createReseau(ip[i],i+1)
        i += 1
    i = 0
    while i < nbRouteur:
        tabReseau = []
        for nb in shema[i]:
            for res in reseaux:
                if res.numero == nb:
                    tabReseau.append(res)
        createRouter(i,tabReseau)
        i+=1
    for routeur in routeurs:
        routeur.work()


def createRouter(numero,listReseau):
    routeurs.append(Routeur(str(numero+1),listReseau))

def createReseau(ip,numero):
    reseaux.append(Reseau(numero,ip))

def imageBackground(nbRouteur):
    global photo
    global canvas
    global button5
    global button6
    photo = PhotoImage(file=path+"/" + str(nbRouteur) + "routeur.png")
    canvas = Canvas(fenetre, width=400, height=400)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.grid(row=1, column=0)
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5 = Button(fenetre, text='Retour', command=lambda: retour())
    button5.grid(row=0, column=0)
    button6 = Button(fenetre, text='Voir la table', command=lambda: openTable())
    button6.grid(row=2, column=0)
    fenetre.geometry("400x450")

def openTable():
    for routeur in routeurs:
        fenetre2 = (Toplevel(fenetre))
        fenetre2.title("Routeur "+routeur.numero)
        scrollbar = Scrollbar(fenetre2)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(fenetre2, yscrollcommand=scrollbar.set)
        for info in routeur.getInfo():
            mylist.insert(END, info)

        mylist.pack(side=LEFT, fill=X)
        scrollbar.config(command=mylist.yview)

        scrollbarIp = Scrollbar(fenetre2)
        scrollbarIp.pack(side=RIGHT, fill=Y)

        mylist = Listbox(fenetre2, yscrollcommand=scrollbarIp.set)
        for interface in routeur.interface:
            str = interface[0]+" adresse ip : "
            i=2
            while i < len(interface):
                if i < len(interface) -1:
                    str += interface[i]+"."
                else:
                    str += interface[i]
                i+=1
            mylist.insert(END, str)
        mylist.pack(side=LEFT, fill=X)
        scrollbarIp.config(command=mylist.yview)



def retour():
    fenetre.geometry("400x20")
    for routeur in routeurs:
        routeur.working = False
    routeurs.clear()
    canvas.destroy()
    button5.destroy()
    button6.destroy()
    createButton()
    resetRouterFolder()

def createButton():
    global button1
    global button2
    global button3
    global button4
    button1 = Button(fenetre, text='1 Routeur', command= lambda: start(1,Shemas.shema1,Shemas.shemaIp1))
    button1.grid(row=0, column=1)
    button2 = Button(fenetre, text='2 Routeurs', command= lambda: start(2,Shemas.shema2,Shemas.shemaIp2))
    button2.grid(row=0, column=2)
    button3 = Button(fenetre, text='3 Routeurs', command= lambda: start(3,Shemas.shema3,Shemas.shemaIp3))
    button3.grid(row=0, column=3)
    button4 = Button(fenetre, text='4 Routeurs', command= lambda: start(4,Shemas.shema4,Shemas.shemaIp4))
    button4.grid(row=0, column=4)

createButton()
fenetre.mainloop()