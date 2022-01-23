from tkinter import Tk,Button,Canvas,Label

#creation d'un objet de type protection
class Protection():

    #initialisation d'un objet de type protection

    #x: coordonnée X de la protection
    #y: coordonnée Y de la protection
    #canvas: canvas créé dans le main
    #lst_protection: liste des blocks initialisée vide

    def __init__(self,x,y,canvas,lst_protection):

        self.lst_protection = lst_protection

        self.canvas = canvas
        self.dimension = (20,20)
        self.vie_block = 1
        self.x = x
        self.y = y
        self.couleur = "brown"
        self.img = None
        
        self.fCreation_bloc()
        
    #creation d'une protection
    def fCreation_bloc(self):
        self.img = self.canvas.create_rectangle(self.x,self.y,self.x+self.dimension[0],self.y+self.dimension[1],fill=self.couleur)

    #destruction d'une protection si collision avec celle-ci
    def fHit(self, pDegat):
        self.vie_block -= pDegat
        if self.vie_block == 0:
            self.fDes_bloc()

    def fDes_bloc(self):
        self.vie = 0
        self.canvas.delete(self.img)
        self.lst_protection.remove(self)