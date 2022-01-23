from tkinter import Tk, Button, Canvas, Label, PhotoImage
from Space_invader_func import fPlay, fNouvelle_partie

fen = Tk()

#creation de la fenetre tkinter:
fen.geometry("850x700+100+50")
fen.title("Les invasionneurs de l'espace")

#creation du canvas:
canvas = Canvas(fen,width = 700, height = 600 , bd=0, bg="black")
canvas.place(x=10,y=50)
canvas.focus_set()

#label pour le titre du score:
label_score_titre = Label(fen, text ="Votre score :")
label_score_titre.place(x=5,y=5)

#initialisation du score a 0:
label_score_chiffre = Label(fen, text ="0")
label_score_chiffre.place(x=100,y=5)

#titre vies restantes
label_vie_titre = Label(fen, text="Nombres de vies restantes :")
label_vie_titre.place(x=500, y=5)

#label nombre de vies
label_vie_chiffre = Label(fen, text= 3)
label_vie_chiffre.place(x=680, y=5)

#label victoire (ou défaite)
label_victoire = Label(fen, text="Victory")
label_defaite = Label(fen, text="You Lose")

#initialisation liste alien et block
liste_alien = []
liste_block = []

vies_vaisseau = 3

#bouton pour quitter la fenetre: 
Bouton_Quitter=Button(fen, text ='Quitter', command = fen.destroy, width=15)
Bouton_Quitter.place(x=725,y=300)

#creation de l'image vaisseau:
img_data = PhotoImage(file = "media/img/vaisseau.png")
img_menu = canvas.create_image(350,550, image = img_data)

#bouton pour faire une nvelle partie
Bouton_Nvlle_Partie=Button(fen, text ='Nouvelle partie', command = lambda: fNouvelle_partie(canvas, liste_alien, liste_block, label_vie_chiffre, label_score_chiffre, vies_vaisseau, fen, label_victoire, label_defaite, Bouton_Nvlle_Partie), width=15)
Bouton_Nvlle_Partie.place(x=725,y=500)

#bouton pour lancer le jeu:
bouton_play = Button(fen, text = 'Play', command = lambda: (fPlay(img_menu, bouton_play, canvas, label_score_chiffre, liste_alien, label_vie_chiffre, liste_block, label_victoire, label_defaite)), width=15, height= 5, foreground="black")
bouton_play.place(x=305, y=300)

fen.mainloop()







