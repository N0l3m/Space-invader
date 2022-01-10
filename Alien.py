from tkinter import Tk,Button,Canvas,Label
import Vaisseau as V
import Balle as b
import random

class Alien():
    
    def __init__(self, pX_alien, pY_alien, pVitesse, pCanvas, pListe_alien, pVaisseau, pLst_protection, pType):

        self.vaisseau = pVaisseau
        self.liste_protection = pLst_protection

        self.list_alien = pListe_alien
        self.vitesse = pVitesse
        self.dimension = (50,50)
        self.couleur_balle = "red"

        self.canvas = pCanvas
        self.type = pType
        self.vie = 1
        self.force = 1
        self.x = pX_alien
        self.y = pY_alien
        if self.type < 2:
            self.img = self.canvas.create_rectangle(self.x,self.y,self.x+self.dimension[0],self.y+self.dimension[1],fill="green")
        else:
            self.img = self.canvas.create_rectangle(self.x,self.y,self.x+self.dimension[0],self.y+self.dimension[1],fill="red")
        self.balle_list = []
        self.vitesse_tir = 0.2
        self.reload = True
        
        self.fMvmt_alien()
        self.fReloading()
        self.vaisseau.fCollision_alien()

    #fonction qui met en mouvement l'alien
    def fMvmt_alien(self):     
        if self.vie >= 1:
            
            self.x += self.vitesse
            
            if self.x >= 650:
                self.vitesse = -self.vitesse
                self.y +=50
                
            elif self.x<5:
                self.vitesse = -self.vitesse
                self.y +=50
 
            self.canvas.coords(self.img, self.x, self.y, self.x+50, self.y+50)
            self.canvas.after(25, self.fMvmt_alien)
            self.fDes_alien()
            self.vaisseau.fCollision_alien()

    #fonction qui fait perdre de la vie en cas de collision avec un objet ennemi
    def fHit(self, pDegat, indice):
        self.vie -= pDegat
        if self.vie <= 0:
            self.canvas.delete(self.img)
            self.list_alien.pop(indice)

    #fonction qui fait tirer l'alien de niveau 1 ou plus
    def fTir_alien(self):
        if self.reload and self.vie > 0 and self.y<=350 and self.type >= 1:
            self.reload = False
            if self.type == 1:
                self.fCrea_balle()
            if self.type == 2:
                self.fCrea_balle_speciale()
            self.fReloading()

    #fonction qui permet un tir de cadence aléatoire entre 2 et 3 secondes
    def fReloading(self):
        self.reload = True
        if self.type == 1:
            self.canvas.after(random.randint(3000,7000),self.fTir_alien)
        if self.type == 2:
            self.canvas.after(random.randint(2000,3000),self.fTir_alien)

    #creation de la balle d'alien
    def fCrea_balle(self):
        self.balle_list.append(b.Balle(self.x+self.dimension[0]/2, self.y+self.dimension[1], self.vitesse_tir, self.force, 1, self.canvas, self.list_alien, self.vaisseau, self.balle_list, self.couleur_balle, self.liste_protection, self.type, 0))

    #creation de la balle d'alien special
    def fCrea_balle_speciale(self):
        self.balle_list.append(b.Balle(self.x+self.dimension[0]/2, self.y+self.dimension[1], self.vitesse_tir, self.force, 1, self.canvas, self.list_alien, self.vaisseau, self.balle_list, self.couleur_balle, self.liste_protection, self.type, 1))
        self.balle_list.append(b.Balle(self.x+self.dimension[0]/2, self.y+self.dimension[1], self.vitesse_tir, self.force, 1, self.canvas, self.list_alien, self.vaisseau, self.balle_list, self.couleur_balle, self.liste_protection, self.type, 0))
        self.balle_list.append(b.Balle(self.x+self.dimension[0]/2, self.y+self.dimension[1], self.vitesse_tir, self.force, 1, self.canvas, self.list_alien, self.vaisseau, self.balle_list, self.couleur_balle, self.liste_protection, self.type, -1))
    
    #destruction de l'alien en cas de sortie de l'ecran
    def fDes_alien(self):
        if self.y>=550:
            self.canvas.delete(self.img)
            self.vie = 0


