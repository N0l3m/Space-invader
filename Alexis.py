from tkinter import Tk,Button,Canvas,Label

from Heather import Canevas

class cvaisseau():
    def __init__(self,pX_vaisseau,pY_vaisseau):
        self.__vie = 10
        self.__force = 5
        self.__posX = pX_vaisseau
        self.__posY = pY_vaisseau



    def fMouvement_vaisseau(self, event):
        touche = event.keysym
        if touche == 'Right'and self.__posX<=650:
            self.__posX += 5
            canvas.coords(vaisseau,self.__posX,self.__posY,self.__posX+50,self.__posY+50)
        if touche == 'Left' and self.__posX>=0:
            self.__posX -= 5
            canvas.coords(vaisseau,self.__posX,self.__posY,self.__posX+50,self.__posY+50)


class calien():
    def __init__(self,pX_alien,pY_alien,pVitesse):
        self.__vie = 10
        self.__posX = pX_alien
        self.__posY = pY_alien
        self.__vitesse = pVitesse

    def fMvmt_alien(self):

        alien = None
    
        self.__posX += self.__vitesse
        
        if self.__posX >= 130:
            self.__vitesse = -self.__vitesse
            self.__posY +=3
        elif self.__posX<5:
            self.__vitesse = -self.__vitesse
            self.__posY +=3
        canvas.delete(alien)
        alien=canvas.create_rectangle(self.__posX, self.__posY, self.__posX+c, self.__posY+c, fill='blue violet', outline='')
        fen.after(50, calien.fMvmt_alien, alien)
        

        


    
        


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
vitesse_alien = 10

vaisseau = canvas.create_rectangle(325,525,325+50,525+50,fill='white')
 
Bouton_Quitter=Button(fen, text ='Quitter', command = fen.destroy, width=15)
Bouton_Quitter.place(x=725,y=300)

Bouton_Nvlle_Partie=Button(fen, text ='Nouvelle partie', command = canvas.update(), width=15)
Bouton_Nvlle_Partie.place(x=725,y=500)

vaisseau_init = cvaisseau(X_vaisseau, Y_vaisseau)

canvas.bind('<Key>', vaisseau_init.fMouvement_vaisseau) 



fen.mainloop()
