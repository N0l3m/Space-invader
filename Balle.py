#class permettant la création d'un objet de type balle
class Balle():

    #initialisation d'un objet de type balle

    #x: coordonnée X de la balle
    #y: coordonnée Y de la balle
    #vitesse: vitesse de la balle
    #force: degats de la balle
    #dir: definit la direction de la balle, il vaut 1 si la balle est alien et -1 si elle est du vaisseau
    #canvas: canvas créé dans le programme principal
    #liste_alien: liste contenants les objets aliens
    #vaisseau: objet vaisseau
    #lst_balle: liste des balles de l'objet associé
    #couleur_balle: couleur de la balle (bleu si vaisseau, rouge si alien)
    #lst_protection: liste des blocks de protection
    #type: permet de savoir si le tireur est un vaisseau ou un alien de type 0, 1 ou 2
    #diag: pour l'alien de type 2, son tir es tcomposé de 3 balles: un vertical et deux diagonnaux symétriques par rapport au premier


    def __init__(self, x, y, vitesse, force, dir, canvas, liste_alien, vaisseau, lst_balle, couleur_balle, lst_protection, type, diag):
        
        self.x = x
        self.y = y+dir*10
        self.force = force
        self.vitesse = vitesse
        self.dir = dir
        self.diagonale = diag
        self.canvas = canvas

        self.dimension = (4,20)

        self.lst_balle = lst_balle
        self.lst_balle_speciale = []
        self.couleur = couleur_balle
        self.liste_alien = liste_alien
        self.vaisseau = vaisseau
        self.liste_protection = lst_protection
        self.type = type
        if self.type == 2:
            self.img = self.canvas.create_oval(self.x, self.y, self.x+10, self.y+10, fill = "red")
        if self.type == 1:
            self.img = self.canvas.create_rectangle(self.x, self.y, self.x+self.dimension[0], self.y-self.dimension[1], fill = self.couleur)
        if self.type == "v":
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
                self.canvas.after(20, lambda : self.fMvmt_balle())

            else:
                self.canvas.delete(self.img)

    #fonction qui gere la collision d'une balle
    def fCollision(self):
        #collision balle d'alien/vaisseau et balle d'alien/blocks de protection
        if self.dir == 1:
            if self.vaisseau.y-self.vaisseau.dimension[1] <= self.y <= self.vaisseau.y+self.vaisseau.dimension[1]:
                if self.vaisseau.x-self.vaisseau.dimension[1] <= self.x <= self.vaisseau.x+self.vaisseau.dimension[0]:
                    self.canvas.delete(self.img)
                    self.vaisseau.fHit(self.force)
                    self.bouge = False
                    self.lst_balle.remove(self)
                    self.vaisseau.fMaj_vie()

            for i,block in enumerate(self.liste_protection):
                if block.y <= self.y <= block.y+block.dimension[1]:   
                    if block.x <= self.x <= block.x+block.dimension[0]:
                        self.canvas.delete(self.img)
                        block.fHit(self.force)
                        self.bouge = False
                        self.lst_balle.remove(self)
            
        #collision balle de vaisseau/alien et balle de vaisseau/blocks de protection
        if self.dir == -1:
            for i,alien in enumerate(self.liste_alien):
                if self.bouge and alien.y-alien.dimension[1] <= self.y <= alien.y+alien.dimension[1]:   
                    if alien.x-alien.dimension[0] <= self.x <= alien.x+alien.dimension[0]:
                        self.canvas.delete(self.img)
                        alien.fHit(self.force, i)
                        self.bouge = False
                        self.lst_balle.remove(self)
                        self.vaisseau.nb_alien_mort += 1
                        if alien.type == 0:
                            self.vaisseau.score += 10
                        if alien.type == 1:
                            self.vaisseau.score += 25
                        if alien.type == 2:
                            self.vaisseau.score += 150
                        self.vaisseau.fMaj_score()

            for i,block in enumerate(self.liste_protection):
                 if self.bouge and block.y + self.dimension[1] <= self.y <= block.y+2*block.dimension[1]:   
                    if block.x <= self.x <= block.x+block.dimension[0]:
                        self.canvas.delete(self.img)
                        self.bouge = False
                        self.lst_balle.remove(self)
    
    #fonction qui detruit la balle
    def fDes_balle(self):
        if self.y>=600 or self.y<=0:
            self.bouge = False
            self.lst_balle.remove(self) 
    
    #fonction qui gere le mvmt des trois balles apres le splir de la balle speciale
    def fMvmt_special(self):
        self.fCollision()
        if self.bouge and self.type == 2:
            if 0 <= self.y <= 600 and 0<= self.x <= 700:
                self.y += self.vitesse
                self.x += (self.vitesse*self.diagonale)
                self.canvas.coords(self.img, self.x, self.y, self.x+10, self.y-10)
                self.canvas.after(20, lambda : self.fMvmt_special())
            else:
                self.bouge = False
                self.canvas.delete(self.img)






