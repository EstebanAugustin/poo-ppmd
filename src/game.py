import re

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
        
        
    def launch(self):
        """
        Lance une partie de démineur
        """
        self.show()
        selected_square, selected_action = self.ask_player(first_turn=True)
        self.grid.generate(selected_square[0], selected_square[1])
        
        
        while self.grid.count_squares() > 0:
            self.show()
            selected_square, selected_action = self.ask_player()
            
            if selected_action == "1":
                square_is_mined = self.reveal_grid_square(selected_square[0], selected_square[1])
                
                if square_is_mined :
                    print("Perdu")
                    return
            
            elif selected_action == "2":
                self.mark_grid_square(selected_square[0], selected_square[1])
        
        print("Gagné")
            
    
    def ask_player(self, first_turn=False):
        """
        Demande au joueur l'action à effectuer :
        - dévoiler une case
        - marquer une case
        """
        ask_square = "Sélectionnez une case i,j "
        
        if first_turn:
            ask_square += "à dévoiler"
        ask_square += "\n"
        ask_square += "Exemple: case de la 3ème colonne de la 2ème ligne, entrer \"2,3\"\n"
        ask_square += ">>> "
        
        answer_pattern = r"^\s*(\d+)\s*,\s*(\d+)\s*$"
        match = None
        
        while match is None:
            answer_square = input(ask_square)
            match = re.match(answer_pattern, answer_square)
            if match is None:
                print("Saisie invalide.\n")
                
        selected_square = [int(match.group(1))-1, int(match.group(2))-1]

        if first_turn:
            selected_action = "1"
        
        else:
            authorized_actions = ["1", "2"]
            ask_action = "Dévoiler la case (1)\n"
            ask_action += "Marquer la case (2)\n"
            ask_action += ">>> "
            
            selected_action = None
            
            while selected_action not in authorized_actions:
                selected_action = input(ask_action)
                if selected_action not in authorized_actions:
                    print("Saisie invalide.\n")
        
        return (selected_square, selected_action)
    
    def reveal_grid_square(self, row, col):
        """
        Révèle une case de la grille
        """
        return self.grid.reveal_square(row, col)
        
    def mark_grid_square(self, row, col):
        """
        Marque une case de la grille
        """
        return self.grid.mark_square(row, col)
    
    def show(self):
        """
        Affiche la partie dans la console
        """
        self.grid.show()
        
    def end(self):
        """
        Affiche le message de fin de partie
        dans la console
        """
        return
        
if __name__ == "__main__":
    game = Game()
    game.launch()