class Balle():
    def __init__(self, pX, pY, pVitesse, pForce, pDir, pCanvas, pList_alien, pVaiseau, pLst_balle, pCouleur_balle, pLst_protection):
        """
        le parametre dir definit la direction de la balle, il vaut 1 si la balle est alien et -1 si elle est du vaisseau
        """
        self.x = pX
        self.y = pY
        self.force = pForce
        self.vitesse = pVitesse
        self.dir = pDir
        self.canvas = pCanvas

        self.dimension = (4,20)

        self.lst_balle = pLst_balle
        self.liste_alien = pList_alien
        self.vaisseau = pVaiseau
        self.liste_protection = pLst_protection

        self.img = self.canvas.create_rectangle(self.x, self.y, self.x+self.dimension[0], self.y-self.dimension[1], fill = pCouleur_balle)
        self.bouge = True
        self.fMvmt_balle()
        self.fDes_balle()


    def fMvmt_balle(self):
        self.fCollision()
        if self.bouge:
            if self.y >= 0 and self.y <= 600:
                self.y += self.vitesse*self.dir
                self.canvas.coords(self.img, self.x, self.y, self.x+self.dimension[0], self.y-self.dimension[1])
                self.canvas.after(1, lambda : self.fMvmt_balle())

            else:
                self.canvas.delete(self.img)

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
                        self.vaisseau.score += 10
                        self.vaisseau.nb_alien_mort += 1
                        self.vaisseau.fMaj_score()

    def fDes_balle(self):
        if self.y>=600 or self.y<=0:
            self.bouge = False
            self.lst_balle.remove(self)
