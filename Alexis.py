from tkinter import Tk,Button,Canvas,Label,PhotoImage

class cvaisseau():
    def __init__(self,pX_vaisseau,pY_vaisseau):
        self.__vie = 10
        self.__force = 5
        self.__pos_vaisseau_X = pX_vaisseau
        self.__pos_vaisseau_Y = pY_vaisseau
        
        
        self.__pos_balle_X = pX_vaisseau
        self.__pos_balle_Y = pY_vaisseau
        self.__temps = 0

        cvaisseau.balle = None
        cvaisseau.disp_balle = 0
        cvaisseau.pos_vaisseau_X = 0
        cvaisseau.pos_vaisseau_Y = 0
        cvaisseau.pos_X = 0 
        cvaisseau.pos_Y = 0

        
    def fMouvement_vaisseau(self, event):
        touche = event.keysym
        if touche == 'Right'and self.__pos_vaisseau_X<=650:
            self.__pos_vaisseau_X += 10
            self.__pos_balle_X += 5
            canvas.coords(vaisseau,self.__pos_vaisseau_X,self.__pos_vaisseau_Y,self.__pos_vaisseau_X+50,self.__pos_vaisseau_Y+50)
        if touche == 'Left' and self.__pos_vaisseau_X>=0:
            self.__pos_vaisseau_X -= 10
            self.__pos_balle_X -= 5
            canvas.coords(vaisseau,self.__pos_vaisseau_X,self.__pos_vaisseau_Y,self.__pos_vaisseau_X+50,self.__pos_vaisseau_Y+50)

        cvaisseau.pos_X = self.__pos_vaisseau_X
        cvaisseau.pos_Y = self.__pos_vaisseau_Y
        
    def fTir(self, event):
        if self.__temps == 0:
            self.__temps = 1
            cvaisseau.balle = canvas.create_rectangle(self.__pos_balle_X,self.__pos_balle_Y,self.__pos_balle_X+4,self.__pos_balle_Y+20,fill = "blue")
            self.fMvmt_balle(self.__pos_vaisseau_X + 23, self.__pos_balle_Y)

    def fPos_balle(self, pX, pY):

        cvaisseau.pos_X = pX
        cvaisseau.pos_Y = pY

        return pX,pY
    
    
        
    def fMvmt_balle(self,pX,pY):

        if pY >= 0:
            pY -= 0.5
            canvas.coords(cvaisseau.balle,pX,pY,pX+4,pY+20)
            fen.after(1,lambda:self.fMvmt_balle(pX,pY))

        if pY == 0:
            canvas.delete(cvaisseau.balle)
            self.__temps = 0
        
        self.fPos_balle(pX,pY)

        return pX,pY
      


class calien(cvaisseau):
    
    def __init__(self,pX_alien,pY_alien,pVitesse):
        
        self.__vie = 1
        self.__posX = pX_alien
        self.__posY = pY_alien
        self.__vitesse = pVitesse
        self.__alien = None 


        

    def fMvmt_alien(self):

        if self.__vie == 1:

            self.__posX += self.__vitesse
            
            if self.__posX >= 650:
                self.__vitesse = -self.__vitesse
                self.__posY +=50
                
            elif self.__posX<5:
                self.__vitesse = -self.__vitesse
                self.__posY +=50

            canvas.delete(self.__alien)
            self.__alien = canvas.create_rectangle(self.__posX,self.__posY,self.__posX+50,self.__posY+50,fill="green")
            fen.after(25, self.fMvmt_alien)
            calien.fCollision(self)

        return(self.__posX,self.__posY)
        
    def fCollision(self):

        if self.__posY<=cvaisseau.pos_Y<=self.__posY+50 and self.__posX-5<=cvaisseau.pos_X<=self.__posX+55 :

            canvas.delete(self.__alien)
            canvas.delete(cvaisseau.balle)
            
            self.__vie = 0
    
    

    



def fPlay():

    X_alien = 325
    Y_alien = 50
    vitesse_alien = 2.5
    nb_alien = 7

    vaisseau_init = cvaisseau(X_vaisseau, Y_vaisseau)

    nb_ligne_alien = int(nb_alien/7)

    for n in range(nb_alien):
        
        if n<4:
            calien(X_alien+n*100,Y_alien,vitesse_alien).fMvmt_alien()  
        if 4<=n<=7:
            calien(X_alien-(nb_alien-n)*100,Y_alien,vitesse_alien).fMvmt_alien() 

    #print("c",72%7)
    #print("d",int(72/7))


    canvas.bind('<space>',vaisseau_init.fTir)

    canvas.bind('<Key>', vaisseau_init.fMouvement_vaisseau) 
    
    bouton_play.destroy() 


fen = Tk()

fen.geometry("850x700+100+50")
fen.title("Les invasionneurs de l'espace")

label_score = Label(fen, text ="Votre score")
label_score.place(x=5,y=5)

canvas = Canvas(fen,width = 700, height = 600 , bd=0, bg="black")
canvas.place(x=10,y=50)
canvas.focus_set()

X_vaisseau = 325
Y_vaisseau = 525
 
Bouton_Quitter=Button(fen, text ='Quitter', command = fen.destroy, width=15)
Bouton_Quitter.place(x=725,y=300)

Bouton_Nvlle_Partie=Button(fen, text ='Nouvelle partie', command = canvas.update(), width=15)
Bouton_Nvlle_Partie.place(x=725,y=500)

vaisseau = canvas.create_rectangle(325,525,325+50,525+50,fill='white')

bouton_play = Button(fen, text = 'Play', command=lambda: (fPlay()), width=15, height= 5, foreground="black")
bouton_play.place(x=305,y=300)

fen.mainloop()



