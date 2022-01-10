from tkinter import Canvas
import Vaisseau as v
import Alien as a
import Protection as pr
import Partie as pa

#fonction qui lance le jeu
def fPlay(pVaisseau, pBouton, pCanvas, pFen, pScore, pLst_alien):

    #conditions initiales du jeu
    nb_alien = 7
    type = (0,1,2)
    X_alien = 325
    Y_alien = 70
    vitesse_alien = 2
    vitesse_alien_special = 1
    nb_de_block = 3
    espacement_protection = 700/nb_de_block


    #creation des objet alien
    liste_alien = pLst_alien

    #creation des objets blocks
    liste_block = []

    #creation de l'objet vaisseau
    vaisseau_jeu = v.Vaisseau(325, 525, pCanvas, liste_alien, liste_block, pScore)

    #creation des alien de maniere ordonnée avec la classe calien:
    nombre_alien_derniere_ligne = nb_alien%7 
    nombre_de_ligne = int(nb_alien/7)
    
    if nombre_alien_derniere_ligne != 0:
        for n in range(nombre_alien_derniere_ligne):
            
            if n<4:
                liste_alien.append(a.Alien(X_alien+n*100,Y_alien+100*(nombre_de_ligne),vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[1]))
            if 4<=n<=7:
                liste_alien.append(a.Alien(X_alien-(nb_alien-n)*100,Y_alien+100*(nombre_de_ligne),vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[1]))
    
    for m in range(nombre_de_ligne):
        if m == nombre_de_ligne - 1:
            for al in range(7):
                if al<4:
                    liste_alien.append(a.Alien(X_alien+al*100,Y_alien+100*m,vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[1]))
                if 4<=al<=7:
                    liste_alien.append(a.Alien(X_alien-(7-al)*100,Y_alien+100*m,vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[1]))
        else:
            for al in range(7):
                
                if al<4:
                    liste_alien.append(a.Alien(X_alien+al*100,Y_alien+100*m,vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[0]))
                if 4<=al<=7:
                    liste_alien.append(a.Alien(X_alien-(7-al)*100,Y_alien+100*m,vitesse_alien,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[0]))

    liste_alien.append(a.Alien(325, 10, vitesse_alien_special,pCanvas, liste_alien, vaisseau_jeu, liste_block, type[2]))

    #creation des protections
    for B in range(nb_de_block):

        for l in range(3):
            for b in range(5):
                liste_block.append(pr.Protection(100 + 200*B+20*b,400+l*20,pCanvas, liste_block))

    #parametres de partie (gagne,perdu,score etc)
    partie = pa.Partie(liste_alien, vaisseau_jeu, pCanvas, pFen, pScore)


    #detection des touches espaces et fleches gaucche et droite pour le tir et le mouvement du vaisseau:
    pCanvas.bind('<space>',vaisseau_jeu.fTir)
    pCanvas.bind('<Key>', vaisseau_jeu.fMouvement_vaisseau) 
    
    #destruction du bouton Play avant de commencer le jeu 
    pBouton.destroy()
    pCanvas.delete(pVaisseau)

    game_on="false"


def fNouvelle_partie(pCanvas, pLst_alien):

    for alien in liste_alien:
        liste_alien.remove(alien)

    vaisseau_jeu = pCanvas.create_rectangle(325, 525, 325+50, 525+50, fill='white')
