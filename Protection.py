from tkinter import Tk,Button,Canvas,Label


class Protection():

    def __init__(self,pPos_block_X,pPos_block_Y,pCanvas,pLst_protection):

        self.lst_protection = pLst_protection

        self.canvas = pCanvas
        self.dimension = (20,20)
        self.vie_block = 1
        self.x = pPos_block_X
        self.y = pPos_block_Y
        self.couleur = "brown"
        self.img = None
        
        self.fCreation_block()
        

    def fCreation_block(self):
        self.img = self.canvas.create_rectangle(self.x,self.y,self.x+self.dimension[0],self.y+self.dimension[1],fill=self.couleur)

    def fHit(self, pDegat, pIndice):
        self.vie_block -= pDegat
        if self.vie_block == 0:
            self.fDes_block()

    def fDes_block(self):
        self.vie = 0
        self.canvas.delete(self.img)
        self.lst_protection.remove(self)