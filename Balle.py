class Balle():
    def __init__(self, pX, pY, pVitesse, pForce, pDir, pCanvas, pList_alien, pVaiseau, pLst_balle, pCouleur_balle, pLst_protection, pType, pDiag):
        """
        le parametre dir definit la direction de la balle, il vaut 1 si la balle est alien et -1 si elle est du vaisseau
        """
        self.x = pX
        self.y = pY
        self.force = pForce
        self.vitesse = pVitesse
        self.dir = pDir
        self.diagonale = pDiag
        self.canvas = pCanvas

        self.dimension = (4,20)

        self.lst_balle = pLst_balle
        self.lst_balle_speciale = []
        self.couleur = pCouleur_balle
        self.liste_alien = pList_alien
        self.vaisseau = pVaiseau
        self.liste_protection = pLst_protection
        self.type = pType
        if self.type == 2:
            self.img = self.canvas.create_oval(self.x, self.y, self.x+10, self.y+10, fill = "red")
        else:
            self.img = self.canvas.create_rectangle(self.x, self.y, self.x+self.dimension[0], self.y-self.dimension[1], fill = self.couleur)
        self.bouge = True
        self.fMvmt_balle()
        self.fMvmt_special()
        self.fDes_balle()

    #fonction responsable du mvmt lineaire des balles des alien de niveau 1
    def fMvmt_balle(self):
        self.fCollision()
        if self.bouge and self.type == 1 or self.type == "v":
            if 0<= self.y <= 600:
                self.y += self.vitesse*self.dir
                self.canvas.coords(self.img, self.x, self.y, self.x+self.dimension[0], self.y-self.dimension[1])
                self.canvas.after(1, lambda : self.fMvmt_balle())

            else:
                self.canvas.delete(self.img)

    #fonction qui gere la collision balle d'alien/vaisseau et balle de vaisseau/alien
    def fCollision(self):
        if self.dir == 1:
            if self.vaisseau.y <= self.y <= self.vaisseau.y+self.vaisseau.dimension[1]:
                if self.vaisseau.x <= self.x <= self.vaisseau.x+self.vaisseau.dimension[0]:
                    self.canvas.delete(self.img)
                    self.vaisseau.fHit(self.force)
                    self.bouge = False
                    self.lst_balle.remove(self)

            for i,block in enumerate(self.liste_protection):
                if block.y <= self.y <= block.y+block.dimension[1]:   
                    if block.x <= self.x <= block.x+block.dimension[0]:
                        self.canvas.delete(self.img)
                        block.fHit(self.force, i)
                        self.bouge = False
                        self.lst_balle.remove(self)
            

        if self.dir == -1:
            for i,alien in enumerate(self.liste_alien):
                if alien.y <= self.y <= alien.y+alien.dimension[1]:   
                    if alien.x <= self.x <= alien.x+alien.dimension[0]:
                        self.canvas.delete(self.img)
                        alien.fHit(self.force, i)
                        self.bouge = False
                        self.lst_balle.remove(self)
                        self.vaisseau.nb_alien_mort += 1
                        if alien.type == 0:
                            self.vaisseau.score += 10
                        if alien.type == 1:
                            self.vaisseau.score += 25
                        if self.vaisseau.score == 2:
                            self.vaisseau += 150
                        self.vaisseau.fMaj_score()

            for i,block in enumerate(self.liste_protection):
                 if self.bouge and block.y + self.dimension[1] <= self.y <= block.y+2*block.dimension[1]:   
                    if block.x <= self.x <= block.x+block.dimension[0]:
                        self.canvas.delete(self.img)
                        self.bouge = False
                        print(self.bouge, 'a supprimer (',i,') :', self)
                        self.lst_balle.remove(self)
    
    #fonction qui detruit la balle
    def fDes_balle(self):
        if self.y>=600 or self.y<=0:
            self.bouge = False
            self.lst_balle.remove(self)

    #fonction qui lance le tire special de l'alien de niveau 2
    
    
    #fonction qui gere le mvmt des trois balles apres le splir de la balle speciale
    def fMvmt_special(self):
        self.fCollision()
        if self.bouge and self.type == 2:
            if 0 <= self.y <= 600 and 0<= self.x <= 700:
                self.y += self.vitesse
                self.x += (self.vitesse*self.diagonale)
                self.canvas.coords(self.img, self.x, self.y, self.x+10, self.y-10)
                self.canvas.after(1, lambda : self.fMvmt_special())
            else:
                self.bouge = False
                self.canvas.delete(self.img)






