from tkinter import Tk,Button,Canvas,Label,PhotoImage,Image
import Balle as b
import Alien as a

#class permettant la création d'un objet de type vaisseau
class Vaisseau():

    #initialisation d'un objet de type vaisseau

    #x: coordonnée X du vaisseau
    #y: coordonnée Y du vaisseau
    #canvas: canvas créé dans le main
    #liste_alien: liste des alien
    #lst_protection: liste des blocks initialisée vide
    #score: score du joueur
    #vie_label: label de la vie initialisée à 3
    #label_victoire: label de victoire qui n'est placé sur le canvas seulement lorsque le joueur a gagné
    #label_defaite: label de victoire qui n'est placé sur le canvas seulement lorsque le joueur a perdu

    def __init__(self, x, y, canvas, liste_alien, lst_protection, score_label, vie_label, label_victoire, label_defaite):

        self.liste_protection = lst_protection

        self.x = x
        self.y = y
        self.dimension = (25,25)
        self.couleur_balle = "blue"

        #permet lors du tir de différentier les aliens du vaisseau
        self.type = "v"

        self.canvas = canvas
        self.img_data = PhotoImage(file = "media/img/vaisseau.png")
        self.img = self.canvas.create_image(self.x,self.y, image = self.img_data)

        #dégats infligés par le vaisseau à un ennemi lorsque il touche sa cible
        self.force = 5
        self.temps_de_recharge = 800
        self.vie = 3
        self.vitesse_tir = 6
        self.reload = True
        self.balle_list = []
        self.list_alien = liste_alien

        self.score = 0
        self.score_label = score_label
        self.vie_label = vie_label
        self.label_victoire = label_victoire
        self.label_defaite = label_defaite
        self.nb_alien_mort = 0

    #mise en mouvement par un bind dans le programme principal avec les flèches du clavier droite et gauche
    def fMouvement_vaisseau(self, event):
        touche = event.keysym

        if touche == 'Right'and self.x <= 650:
            self.x += 10
            self.canvas.coords(self.img,self.x,self.y)

        if touche == 'Left' and self.x>=0:
            self.x -= 10
            self.canvas.coords(self.img,self.x,self.y)
        
    #tir déclenché par une pression sur la barre espace grace à un bind dans le programme principal 
    def fTir(self, event):
        if self.reload and self.vie>=0:
            self.reload = False
            self.balle_list.append(b.Balle(self.x, self.y, self.vitesse_tir, self.force, -1, self.canvas, self.list_alien, self, self.balle_list, self.couleur_balle, self.liste_protection, self.type, 0))
            self.canvas.after(self.temps_de_recharge, lambda: self.reloading())

    #rechargement d'une balle
    def reloading(self):
        self.reload = True

    #collision du vaisseau avec un objet qui lui retire pDegat (un nombre de point de vie)
    def fHit(self, pDegat):
        self.vie -= pDegat
        self.fVictoire()
        self.fMaj_vie()
        if self.vie == 0:
            self.canvas.delete(self.img)

    #incrémentation du score lorsque le vaisseau tue un alien
    def fMaj_score(self):
        self.score_label.config(text = self.score)

    #mise à jour de la vie du vaisseau lorsque celui ci percute un objet ennemi ou que la partie recommence
    def fMaj_vie(self):
        self.vie_label.config(text = self.vie)

    #collision du vaisseau avec un alien
    def fCollision_alien(self):
        for alien in self.list_alien:
            if self.x-self.dimension[0]<=alien.x<=self.x+self.dimension[0]:
                if self.y-self.dimension[1]<=alien.y<=self.y+self.dimension[1]:  
                    self.fHit(self.vie) 

    #destruction du vaisseau
    def fDes_vaisseau(self):
        self.vie = 0
        self.canvas.delete(self.img)

    #affichage du label victoire ou defaite respectivement si la liste d'alien est vide ou que la vie du vaisseau est nulle ou négative
    def fVictoire(self):
        if self.list_alien == []:
            self.label_victoire.place(x=350,y=300)
        if self.vie <= 0:
            self.label_defaite.place(x=350,y=300)
