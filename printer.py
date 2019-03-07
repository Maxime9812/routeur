import rout
import os
import shutil
from tkinter import *
from tkinter import messagebox
from functools import partial
import os, sys


fileDirectory = "/Users/" + os.getlogin() + "/Desktop/Routeur/"
shema1 = [[1,2]]
shema2 = [[1,2],[2,3]]
shema3 = [[1,2,4],[2,3,5],[4,5,6,7]]
shema4 = [[1,2,4],[2,3,6],[4,5,7],[8,5,6]]
routeurs = []
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


fenetre.geometry("400x420")
fenetre.resizable(width=False, height=False)
def start(nbRouteur,shema):
    imageBackground(nbRouteur)
    i = 0
    while i < nbRouteur:
        createRouter(i,shema[i])
        i+=1
    for routeur in routeurs:
        routeur.work()
def createRouter(numero,listReseau):
    routeurs.append(rout.rout(str(numero+1),listReseau))

def imageBackground(nbRouteur):
    global photo
    global canvas
    global button5
    photo = PhotoImage(file=path+"/" + str(nbRouteur) + "routeur.png")
    canvas = Canvas(fenetre, width=400, height=400)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.grid(row=1, column=0)
    button5 = Button(fenetre, text='Retour', command=lambda: retour())
    button5.grid(row=0, column=0)
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()


def retour():
    routeurs.clear()
    canvas.destroy()
    button5.destroy()
    createButton()

def createButton():
    global button1
    global button2
    global button3
    global button4
    button1 = Button(fenetre, text='1 Routeur', command= lambda: start(1,shema1))
    button1.grid(row=0, column=1)
    button2 = Button(fenetre, text='2 Routeurs', command= lambda: start(2,shema2))
    button2.grid(row=0, column=2)
    button3 = Button(fenetre, text='3 Routeurs', command= lambda: start(3,shema3))
    button3.grid(row=0, column=3)
    button4 = Button(fenetre, text='4 Routeurs', command= lambda: start(4,shema4))
    button4.grid(row=0, column=4)

createButton()
fenetre.mainloop()
