from tkinter import Tk,Button,Canvas,Label
from timeit import default_timer

class cvaisseau():
    def __init__(self,pX_vaisseau,pY_vaisseau):
        self.__vie = 10
        self.__force = 5
        self.__pos_vaisseau_X = pX_vaisseau
        self.__pos_vaisseau_Y = pY_vaisseau
        
        self.__balle = None
        self.__pos_balle_X = pX_vaisseau
        self.__pos_balle_Y = pY_vaisseau
        self.__temps = 0
        

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
        
        if touche == 'space' and self.__temps == 0:
            self.__temps = 1
            self.__balle = canvas.create_rectangle(self.__pos_balle_X,self.__pos_balle_Y,self.__pos_balle_X+4,self.__pos_balle_Y+20,fill = "blue")
            self.fMvmt_balle(self.__pos_vaisseau_X+23,self.__pos_balle_Y)
        
        return self.__pos_vaisseau_X,self.__pos_vaisseau_Y
        
    def fMvmt_balle(self,pX,pY):
        if pY >= 0:
            pY -= 5
            canvas.coords(self.__balle,pX,pY,pX+4,pY+20)
            fen.after(2,lambda:self.fMvmt_balle(pX,pY))
        if pY == 0:
            canvas.delete(self.__balle)
            self.__temps = 0
    


            


    


class calien():
    def __init__(self,pX_alien,pY_alien,pVitesse):
        self.__vie = 10
        self.__posX = pX_alien
        self.__posY = pY_alien
        self.__vitesse = pVitesse
        self.__alien = None 

    def fMvmt_alien(self):
        
    
        self.__posX += self.__vitesse
        
        if self.__posX >= 650:
            self.__vitesse = -self.__vitesse
            self.__posY +=10
            
        elif self.__posX<5:
            self.__vitesse = -self.__vitesse
            self.__posY +=10
        canvas.delete(self.__alien)
        self.__alien = canvas.create_rectangle(self.__posX,self.__posY,self.__posX+50,self.__posY+50,fill="green")
        fen.after(100, self.fMvmt_alien)
        
def fPlay():

    canvas.bind('<Key>', vaisseau_init.fMouvement_vaisseau) 

    alien_init = calien(X_alien,Y_alien,vitesse_alien)

    alien_init.fMvmt_alien()

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

X_alien = 325
Y_alien = 25
vitesse_alien = 20
 
Bouton_Quitter=Button(fen, text ='Quitter', command = fen.destroy, width=15)
Bouton_Quitter.place(x=725,y=300)

Bouton_Nvlle_Partie=Button(fen, text ='Nouvelle partie', command = canvas.update(), width=15)
Bouton_Nvlle_Partie.place(x=725,y=500)

vaisseau = canvas.create_rectangle(325,525,325+50,525+50,fill='white')

vaisseau_init = cvaisseau(X_vaisseau, Y_vaisseau)

bouton_play = Button(fen, text = 'Play', command = fPlay, width=15, height= 5, foreground="black")
bouton_play.place(x=305,y=300)



fen.mainloop()


