from tkinter import Tk,Button,Canvas,Label
from Space_invader_func import fPlay, fNouvelle_partie

"""
--------------------------------------------------------------------------------------------------------------------------------------
"""

#fonction qui reinitialise le canvas:
def fNvelle_partie(pX_vaisseau,pY_vaisseau):

    global nb_alien,game_on

    if game_on == "false":

        game_on = "true"

        canvas.create_rectangle(700,600,0,0,fill="black")

        nb_alien = 0
        new_vaisseau = canvas.create_rectangle(pX_vaisseau,pY_vaisseau,pX_vaisseau+50,pY_vaisseau+50,fill='white')

        new_bouton_play = Button(fen, text = 'Relay', command = lambda: (fPlay(new_vaisseau,new_bouton_play)), width=15, height= 5, foreground="black")
        new_bouton_play.place(x=305,y=300)

        label_score_chiffre.config(text=0)

"""
--------------------------------------------------------------------------------------------------------------------------------------
"""


fen = Tk()

#creation de la fenetre tkinter:
fen.geometry("850x700+100+50")
fen.title("Les invasionneurs de l'espace")

#creation du canvas:
canvas = Canvas(fen,width = 700, height = 600 , bd=0, bg="black")
canvas.place(x=10,y=50)
canvas.focus_set()

#label pour le titre du score:
label_score_titre = Label(fen, text ="Votre score")
label_score_titre.place(x=5,y=5)

#initialisation du score a 0:
label_score_chiffre = Label(fen, text ="0")
label_score_chiffre.place(x=100,y=5)

liste_alien = []

#bouton pour quitter la fenetre: 
Bouton_Quitter=Button(fen, text ='Quitter', command = fen.destroy, width=15)
Bouton_Quitter.place(x=725,y=300)

#bouton pour faire une nvelle partie
Bouton_Nvlle_Partie=Button(fen, text ='Nouvelle partie', command = lambda: fNouvelle_partie(canvas, liste_alien), width=15)
Bouton_Nvlle_Partie.place(x=725,y=500)

#creation de l'image vaisseau:
vaisseau_menu = canvas.create_rectangle(325, 525, 325+50, 525+50, fill='white')

#bouton pour lancer le jeu:
bouton_play = Button(fen, text = 'Play', command = lambda: (fPlay(vaisseau_menu, bouton_play, canvas, fen, label_score_chiffre, liste_alien)), width=15, height= 5, foreground="black")
bouton_play.place(x=305, y=300)



fen.mainloop()