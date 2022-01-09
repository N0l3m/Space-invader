from tkinter import Tk,Button,Canvas,Label
import Vaisseau as V
import Balle as b
import random

class Alien():
    
    def __init__(self, pX_alien, pY_alien, pVitesse, pCanvas, pListe_alien, pVaisseau, pLst_protection):

        self.vaisseau = pVaisseau
        self.liste_protection = pLst_protection

        self.list_alien = pListe_alien
        self.vitesse = pVitesse
        self.dimension = (50,50)
        self.couleur_balle = "red"

        self.canvas = pCanvas
        self.vie = 1
        self.force = 1
        self.x = pX_alien
        self.y = pY_alien
        self.img = self.canvas.create_rectangle(self.x,self.y,self.x+self.dimension[0],self.y+self.dimension[1],fill="green")

        self.balle_list = []
        self.vitesse_tir = 0.3
        self.reload = True
        
        self.fMvmt_alien()
        self.fReloading()
        self.vaisseau.fCollision_alien()

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


    def fHit(self, pDegat, indice):
        self.vie -= pDegat
        if self.vie <= 0:
            self.canvas.delete(self.img)
            self.list_alien.pop(indice)

    def fTir_alien(self):
        if self.reload and self.vie > 0 and self.y<=350:
            self.reload = False
            self.fCrea_balle()
            self.fReloading()

    def fReloading(self):
        self.reload = True
        self.canvas.after(random.randint(2000,3000),self.fTir_alien)

    def fCrea_balle(self):
        self.balle_list.append(b.Balle(self.x+self.dimension[0]/2, self.y+self.dimension[1], self.vitesse_tir, self.force, 1, self.canvas, self.list_alien, self.vaisseau, self.balle_list, self.couleur_balle, self.liste_protection))

    def fDes_alien(self):
        if self.y>=550:
            self.canvas.delete(self.img)
            self.vie = 0
