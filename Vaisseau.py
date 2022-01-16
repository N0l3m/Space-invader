from tkinter import Tk,Button,Canvas,Label,PhotoImage,Image
import Balle as b
import Alien as a

class Vaisseau():

    def __init__(self, pX_vaisseau, pY_vaisseau, pCanvas, liste_alien, pLst_protection, pScore_label, pVie_label, pLabel_victoire, pLabel_defaite):

        self.liste_protection = pLst_protection

        self.x = pX_vaisseau
        self.y = pY_vaisseau
        self.dimension = (25,25)
        self.couleur_balle = "blue"
        self.type = "v"

        self.canvas = pCanvas
        self.img_data = PhotoImage(file = "media/img/vaisseau.png")
        self.img = self.canvas.create_image(self.x,self.y, image = self.img_data)

        self.force = 5
        self.temps_de_recharge = 800
        self.vie = 3
        self.vitesse_tir = 6
        self.reload = True
        self.balle_list = []
        self.list_alien = liste_alien

        self.score = 0
        self.score_label = pScore_label
        self.vie_label = pVie_label
        self.label_victoire = pLabel_victoire
        self.label_defaite = pLabel_defaite
        self.nb_alien_mort = 0

    def fMouvement_vaisseau(self, event):
        touche = event.keysym

        if touche == 'Right'and self.x <= 650:
            self.x += 10
            self.canvas.coords(self.img,self.x,self.y)

        if touche == 'Left' and self.x>=0:
            self.x -= 10
            self.canvas.coords(self.img,self.x,self.y)
        
        
    def fTir(self, event):
        if self.reload and self.vie>=0:
            self.reload = False
            self.balle_list.append(b.Balle(self.x, self.y, self.vitesse_tir, self.force, -1, self.canvas, self.list_alien, self, self.balle_list, self.couleur_balle, self.liste_protection, self.type, 0))
            self.canvas.after(self.temps_de_recharge, lambda: self.reloading())

    def reloading(self):
        self.reload = True

    def fHit(self, pDegat):
        self.vie -= pDegat
        self.fVictoire()
        if self.vie == 0:
            self.canvas.delete(self.img)

    def fMaj_score(self):
        self.score_label.config(text = self.score)

    def fMaj_vie(self):
        self.vie_label.config(text = self.vie)

    def fCollision_alien(self):
        for alien in self.list_alien:
            if self.x-self.dimension[0]<=alien.x<=self.x+self.dimension[0]:
                if self.y-self.dimension[1]<=alien.y<=self.y+self.dimension[1]:  
                    self.fHit(self.vie) 

    def fDes_vaisseau(self):
        self.vie = 0
        self.canvas.delete(self.img)

    def fVictoire(self):
        if self.list_alien == []:
            self.label_victoire.place(x=350,y=300)
        if self.vie <= 0:
            self.label_defaite.place(x=350,y=300)
