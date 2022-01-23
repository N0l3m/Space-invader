from tkinter import Canvas, Button, Label
import Vaisseau as v
import Alien as a
import Protection as pr


#fonction qui lance le jeu: creation de tous les objets necessaires et aménagement du canvas

#vaisseau: vaisseau initial dans le menu
#bouton: bouton play créé dans le programme principal
#canvas: canvas créé dans le main
#score: score initialisé à 0 dans le programme principal
#lst_alien: liste des alien initialisée vide
#label_vie: label de la vie initialisée à 3
#lst_protection: liste des blocs de protection initialisée vide
#label_victoire: label de victoire qui n'est placé sur le canvas seulement lorsque le joueur a gagné
#label_defaite: label de victoire qui n'est placé sur le canvas seulement lorsque le joueur a perdu

def fPlay(vaisseau, bouton, canvas, score, lst_alien, label_vie, lst_protection, label_victoire, label_defaite):

    global vaisseau_jeu, on_game

    on_game = True

    #conditions initiales du jeu
    nb_alien = 14
    type = (0,1,2)
    X_alien = 350
    Y_alien = 85
    vitesse_alien = 2
    vitesse_alien_special = 1
    nb_de_bloc = 3
    espacement_protection = 700/nb_de_bloc


    #creation des objet alien
    liste_alien = lst_alien

    #creation des objets blocks
    liste_bloc = lst_protection

    #creation de l'objet vaisseau
    vaisseau_jeu = v.Vaisseau(350, 550, canvas, liste_alien, liste_bloc, score, label_vie, label_victoire, label_defaite)

    #creation des alien de maniere ordonnée avec la classe calien:
    nombre_alien_derniere_ligne = nb_alien%7 
    nombre_de_ligne = int(nb_alien/7)
    
    if nombre_alien_derniere_ligne != 0:
        for n in range(nombre_alien_derniere_ligne):
            
            if n<4:
                liste_alien.append(a.Alien(X_alien+n*100,Y_alien+100*(nombre_de_ligne),vitesse_alien,canvas, liste_alien, vaisseau_jeu, liste_bloc, type[1]))
            if 4<=n<=7:
                liste_alien.append(a.Alien(X_alien-(nb_alien-n)*100,Y_alien+100*(nombre_de_ligne),vitesse_alien,canvas, liste_alien, vaisseau_jeu, liste_bloc, type[1]))
    
    for m in range(nombre_de_ligne):
        if m == nombre_de_ligne - 1:
            for al in range(7):
                if al<4:
                    liste_alien.append(a.Alien(X_alien+al*100,Y_alien+100*m,vitesse_alien,canvas, liste_alien, vaisseau_jeu, liste_bloc, type[1]))
                if 4<=al<=7:
                    liste_alien.append(a.Alien(X_alien-(7-al)*100,Y_alien+100*m,vitesse_alien,canvas, liste_alien, vaisseau_jeu, liste_bloc, type[1]))
        else:
            for al in range(7):
                
                if al<4:
                    liste_alien.append(a.Alien(X_alien+al*100,Y_alien+100*m,vitesse_alien,canvas, liste_alien, vaisseau_jeu, liste_bloc, type[0]))
                if 4<=al<=7:
                    liste_alien.append(a.Alien(X_alien-(7-al)*100,Y_alien+100*m,vitesse_alien,canvas, liste_alien, vaisseau_jeu, liste_bloc, type[0]))

    #creation de l'alien special
    liste_alien.append(a.Alien(350, 40, vitesse_alien_special,canvas, liste_alien, vaisseau_jeu, liste_bloc, type[2]))

    #creation des protections
    for B in range(nb_de_bloc):

        for l in range(3):
            for b in range(5):
                liste_bloc.append(pr.Protection(100 + 200*B+20*b,400+l*20,canvas, liste_bloc))


    #detection des touches espaces et fleches gaucche et droite pour le tir et le mouvement du vaisseau:
    canvas.bind('<space>',vaisseau_jeu.fTir)
    canvas.bind('<Key>', vaisseau_jeu.fMouvement_vaisseau) 
    
    #destruction du bouton Play avant de commencer le jeu 
    bouton.destroy()
    canvas.delete(vaisseau)

#fonction qui renouvelle le canvas: réinitialisation des listes d'objets comme la liste d'aliens et de blocks et réinitialisiation du vaisseau
#réinitialisation des labels comme le score la victoire ou la défaite et la vie

#canvas: canvas créé dans le main
#lst_alien: liste des alien initialisée vide
#pLst_block: liste des blocks initialisée vide
#label_vie: label de la vie initialisée à 3
#score: score initialisé à 0 dans le programme principal
#fen: fenetre tkinter
#label_victoire: label de victoire qui n'est placé sur le canvas seulement lorsque le joueur a gagné
#label_defaite: label de victoire qui n'est placé sur le canvas seulement lorsque le joueur a perdu
#bouton: bouton Nouvelle Partie

def fNouvelle_partie(canvas, lst_alien, pLst_block, label_vie, score, vie, fen, label_victoire, label_defaite, bouton):

    global vaisseau_jeu, on_game

    if on_game == True:

        on_game = False

        vaisseau_jeu.fDes_vaisseau()

        while lst_alien != []:
            for alien in lst_alien:
                alien.fDes_alien()

        while pLst_block != []:
            for block in pLst_block:
                block.fDes_bloc()

        label_vie.config(text = vie)
        score.config(text = 0)

        label_defaite.destroy()
        label_victoire.destroy()
        
        new_label_defaite = Label(fen, text="You Lose")
        new_label_victoire = Label(fen, text="Victory")

        bouton.destroy()

        Bouton_Nvlle_Partie=Button(fen, text ='Nouvelle partie', command = lambda: fNouvelle_partie(canvas, lst_alien, pLst_block, label_vie, score, vie, fen, new_label_victoire, new_label_defaite, Bouton_Nvlle_Partie), width=15)
        Bouton_Nvlle_Partie.place(x=725,y=500)
        
        nouveau_vaisseau_menu = canvas.create_rectangle(325, 525, 325+50, 525+50, fill='white')

        new_bouton_play = Button(fen, text = 'Play', command = lambda: (fPlay(nouveau_vaisseau_menu, new_bouton_play, canvas, score, lst_alien, label_vie, pLst_block, new_label_victoire, new_label_defaite)), width=15, height= 5, foreground="black")
        new_bouton_play.place(x=305, y=300)
