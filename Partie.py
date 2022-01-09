class Partie():
    def __init__(self, pLst_alien, pVaisseau, pCanvas, pFen, pScore):

        self.canvas = pCanvas
        self.fen = pFen

        self.lst_alien = pLst_alien
        self.vaisseau = pVaisseau

        self.score = pScore
        self.on_game = False
        self.victoire = False
        print(self.vaisseau.nb_alien_mort)
        self.fMaj_score()

    def fMaj_score(self):
        
        self.score.config(text = 10*self.vaisseau.nb_alien_mort)

    def fInit_score(self):
        if self.on_game == False:
            self.score = 0

    def fFin_partie(self):
        if self.lst_alien == [] or self.vaisseau.vie <= 0:
            self.on_game = False

    
    


