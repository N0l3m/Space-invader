from abc import abstractproperty
from tkinter import Tk, Button, Canvas, Label, Menu
import random

mw = Tk()
mw.geometry('700x500+200+50')
mw.title("Invasionneurs de l'espace")

#Fonctions

def fNewGame():
    Canevas.delete('all')
    

def fQuitter():
    Canevas.delete('all')
    mw.destroy()
    
def fAPropos():
    print("A Propos")

def fAffScore():
    print("Coucou le score")

def fAide():
    print("Aide")

#Fin Fonctions

#Menu
menubar = Menu(mw)
menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label = "A propos",command = fAPropos)
menufichier.add_command(label = "Scores",command = fAffScore)
menubar.add_cascade(label = "Menu",menu = menufichier)
menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label = "Aide",command = fAide)
menubar.add_cascade(label = "Aide",menu = menuaide)

#Affichage Menu
mw.config(menu = menubar)


Largeur = 600
Hauteur = 500
Canevas = Canvas(mw, width = Largeur, height = Hauteur, bg='white')
Canevas.pack(side='bottom',padx = 0, pady = 5)

label_score = Label(mw,text="Score : ")
label_score.pack(side='left',padx=5,pady=5)

label_vies = Label(mw,text="Vies : ")
label_vies.pack(side='right',padx=5,pady=5)

button_nouveau = Button(mw,text="New game",command=fNewGame)
button_nouveau.place(x=650,y=550)

button_quit = Button(mw,text="Quit",command=fQuitter)
button_quit.place(x=650,y=550)

def Cercle(r=10):
    if r<Largeur and r<Hauteur:
        x = 300
        y = 400
        Canevas.create_oval(x-r,y-r,x+r,y+r, fill='red')

Cercle()




mw.mainloop()