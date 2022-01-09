from tkinter import Tk,Button,Canvas,Label
import Balle as b
import Alien as a

class Vaisseau():

    def __init__(self, pX_vaisseau, pY_vaisseau, pCanvas, liste_alien, pLst_protection, pScore_label):

        self.liste_protection = pLst_protection

        self.x = pX_vaisseau
        self.y = pY_vaisseau
        self.dimension = (50,50)
        self.couleur_balle = "blue"

        self.canvas = pCanvas
        self.img = self.canvas.create_rectangle(self.x, self.y, self.x+self.dimension[0], self.y+self.dimension[1], fill='white')
        
        self.force = 5
        self.temps_de_recharge = 800
        self.vie = 3
        self.vitesse_tir = 0.3
        self.reload = True
        self.balle_list = []
        self.list_alien = liste_alien
        self.score = 0
        self.score_label = pScore_label
        self.nb_alien_mort = 0

    def fMouvement_vaisseau(self, event):
        touche = event.keysym

        if touche == 'Right'and self.x <= 650:
            self.x += 10
            self.canvas.coords(self.img,self.x,self.y,self.x+self.dimension[0],self.y+self.dimension[1])

        if touche == 'Left' and self.x>=0:
            self.x -= 10
            self.canvas.coords(self.img,self.x,self.y,self.x+self.dimension[0],self.y+self.dimension[1])
        
        
    def fTir(self, event):
        if self.reload:
            self.reload = False
            self.balle_list.append(b.Balle(self.x+self.dimension[0]/2, self.y, self.vitesse_tir, self.force, -1, self.canvas, self.list_alien, self, self.balle_list, self.couleur_balle, self.liste_protection))
            self.canvas.after(self.temps_de_recharge, lambda: self.reloading())

    def reloading(self):
        self.reload = True

    def fHit(self, pDegat):
        self.vie -= pDegat
        if self.vie == 0:
            self.canvas.delete(self.img)

    def fMaj_score(self):
        self.score_label.config(text = self.score)

    
            