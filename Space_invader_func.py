from tkinter import Canvas, Button
import Vaisseau as v
import Alien as a
import Protection as pr
import Partie as pa

#fonction qui lance le jeu
def fPlay(pVaisseau, pBouton, pCanvas, pFen, pScore, pLst_alien, pVie, pLst_block, pLabel_victoire, pLabel_defaite):

    global vaisseau_jeu

    #conditions initiales du jeu
    nb_alien = 7
    type = (0,1,2)
    X_alien = 350
    Y_alien = 85
    vitesse_alien = 2
    vitesse_alien_special = 1
    nb_de_block = 3
    espacement_protection = 700/nb_de_block


    #creation des objet alien
    liste_alien = pLst_alien

    #creation des objets blocks
    liste_block = pLst_block

    #creation de l'objet vaisseau
    vaisseau_jeu = v.Vaisseau(325, 525, pCanvas, liste_alien, liste_block, pScore, pVie, pLabel_victoire, pLabel_defaite)

    #creation des alien de maniere ordonnée avec la classe calien:
    nombre_alien_derniere_ligne = nb_alien%7 
    nombre_de_ligne = int(nb_alien/7)
    
    if nombre_alien_derniere_ligne != 0:
        for n in range(nombre_alien_derniere_ligne):
            
            if n<4:
                liste_alien.append(a.Alien(X_alien+n*100,Y_alien+100*(nombre_de_ligne),vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[1], pFen))
            if 4<=n<=7:
                liste_alien.append(a.Alien(X_alien-(nb_alien-n)*100,Y_alien+100*(nombre_de_ligne),vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[1], pFen))
    
    for m in range(nombre_de_ligne):
        if m == nombre_de_ligne - 1:
            for al in range(7):
                if al<4:
                    liste_alien.append(a.Alien(X_alien+al*100,Y_alien+100*m,vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[1], pFen))
                if 4<=al<=7:
                    liste_alien.append(a.Alien(X_alien-(7-al)*100,Y_alien+100*m,vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[1], pFen))
        else:
            for al in range(7):
                
                if al<4:
                    liste_alien.append(a.Alien(X_alien+al*100,Y_alien+100*m,vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[0], pFen))
                if 4<=al<=7:
                    liste_alien.append(a.Alien(X_alien-(7-al)*100,Y_alien+100*m,vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[0], pFen))

    liste_alien.append(a.Alien(350, 40, vitesse_alien_special,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[2], pFen))

    #creation des protections
    for B in range(nb_de_block):

        for l in range(3):
            for b in range(5):
                liste_block.append(pr.Protection(100 + 200*B+20*b,400+l*20,pCanvas, liste_block))


    #detection des touches espaces et fleches gaucche et droite pour le tir et le mouvement du vaisseau:
    pCanvas.bind('<space>',vaisseau_jeu.fTir)
    pCanvas.bind('<Key>', vaisseau_jeu.fMouvement_vaisseau) 
    
    #destruction du bouton Play avant de commencer le jeu 
    pBouton.destroy()
    pCanvas.delete(pVaisseau)


def fNouvelle_partie(pCanvas, pLst_alien, pLst_block, pLabel_Vie, pScore, pVie, pFen, pLabel_victoire, pLabel_defaite):

    global vaisseau_jeu

    vaisseau_jeu.fDes_vaisseau()

    while pLst_alien != []:
        for alien in pLst_alien:
            alien.fDes_alien()

    while pLst_block != []:
        for block in pLst_block:
            block.fDes_block()

    pLabel_Vie.config(text = pVie)
    pScore.config(text = 0)
    
    nouveau_vaisseau_menu = pCanvas.create_rectangle(325, 525, 325+50, 525+50, fill='white')

    new_bouton_play = Button(pFen, text = 'Play', command = lambda: (fPlay(nouveau_vaisseau_menu, new_bouton_play, pCanvas, pFen, pScore, pLst_alien, pVie, pLst_block, pLabel_victoire, pLabel_defaite)), width=15, height= 5, foreground="black")
    new_bouton_play.place(x=305, y=300)
