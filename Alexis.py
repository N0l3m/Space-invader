from tkinter import Tk,Button,Canvas,Label

def fMouvement_vaisseau(event):
    global X_vaisseau,Y_vaisseau
    touche = event.keysym
    print(touche)
    if touche == 'Right'and X_vaisseau<=650:
        X_vaisseau += 5
        canvas.coords(vaisseau,X_vaisseau,Y_vaisseau,X_vaisseau+50,Y_vaisseau+50)
        print(X_vaisseau)
    if touche == 'Left' and X_vaisseau>=0:
        X_vaisseau -= 5
        canvas.coords(vaisseau,X_vaisseau,Y_vaisseau,X_vaisseau+50,Y_vaisseau+50)



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

Y_alien = 325
Y_alien = 5

vaisseau = canvas.create_rectangle(X_vaisseau,Y_vaisseau,X_vaisseau+50,Y_vaisseau+50,fill='white')
 
Bouton_Quitter=Button(fen, text ='Quitter', command = fen.destroy, width=15)
Bouton_Quitter.place(x=725,y=300)

Bouton_Nvlle_Partie=Button(fen, text ='Nouvelle partie', command = fen.destroy, width=15)
Bouton_Nvlle_Partie.place(x=725,y=500)

alien = canvas.create_rectangle(Y_alien,Y_alien,Y_alien+50,Y_alien+50,fill='green')

canvas.bind('<Key>', fMouvement_vaisseau)


fen.mainloop()

print("kk")