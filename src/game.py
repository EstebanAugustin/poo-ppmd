from grid import Grid

class Game:
    """
    Instancie une partie de démineur
    """
    
    def __init__(self, level=1):
        self.time = 0.0
        self.level = level
        self.score = 0
        self.grid = Grid()
        
        self.launch()
        
    def launch(self):
        """
        Lance une partie de démineur
        """
        self.show()
        self.ask_player()
    
    def ask_player(self):
        """
        Demande au joueur l'action à effectuer :
        - dévoiler une case
        - marquer une case
        """
        ask_square = "Sélectionnez une case i,j \n"
        ask_square += "Exemple: case de la 3ème colonne de la 2ème ligne, entrer \"2,3\"\n"
        ask_square += ">>> "
        answer_square = input(ask_square)
        
        ask_action = "Dévoiler la case (1)\nMarquer la case (2)\n>>> "
        answer_action = input(ask_action)
    
    def reveal_grid_square(self):
        """
        Révèle une case de la grille
        """
        return
        
    def mark_grid_square(self):
        """
        Marque une case de la grille
        """
        return
    
    def show(self):
        """
        Affiche la partie dans la console
        """
        grid_str = self.grid.show()
        print(grid_str, flush=True)
        
    def end(self):
        """
        Affiche le message de fin de partie
        dans la console
        """
        return
        
if __name__ == "__main__":
    game = Game()
    game.show()