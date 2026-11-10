import re

from grid import Grid

class Game:
    """
    Partie de démineur.
    
    ...
    
    Attributs
    ---------
    time : int, default=0
        Temps écoulé de la partie.
    level : int, default=1
        Niveau de difficulté de la partie (1 à 3).
    score : int, default=0
        Score du joueur.
    grid : Grid
        Grille de la partie.
    
    Méthodes
    --------
    launch()
        Lance une partie de démineur.
    _ask_player(first_turn=False)
        Demande au joueur l'action à effectuer.
    reveal_grid_square(row, col)
        Révèle une case de la grille.
    mark_grid_square(row, col)
        Marque une case de la grille.
    show()
        Affiche la partie dans la console.
    """
    
    LEVELS = {
        1: {"n_rows": 9,  "n_cols": 9,  "n_mines": 10},
        2: {"n_rows": 16, "n_cols": 16, "n_mines": 40},
        3: {"n_rows": 16, "n_cols": 30, "n_mines": 99},
    }
    
    def __init__(self, level=1):
        if level not in Game.LEVELS:
            raise ValueError("level doit être 1, 2 ou 3.")
        self.time = 0
        self.level = level
        self.score = 0
        config = Game.LEVELS[level]
        self.grid = Grid(
            n_rows=config["n_rows"],
            n_cols=config["n_cols"],
            n_mines=config["n_mines"]
        )
        
        
    def launch(self):
        """
        Lance une partie de démineur.
        
        ...
        
        Règles
        ------
        - Au premier tour, la case sélectionnée est forcément dévoilée
        et les mines sont placées en conséquence.
        - La partie est perdue si le joueur dévoile une case minée.
        - La partie est gagnée si toutes les cases non minées sont
        découvertes.
        """
        self.show()
        
        selected_square, selected_action = self._ask_player(
            first_turn=True
        )
        
        square_row, square_col = selected_square
        
        self.grid.prepare(
            excluded_row=square_row,
            excluded_col=square_col
        )
        
        self._reveal_grid_square(square_row, square_col)
        
        while self.grid.count_safe_squares_left() > 0:
            self.show()
            selected_square, selected_action = self._ask_player()
            square_row, square_col = selected_square
            
            if selected_action == "1":
                revealed = self._reveal_grid_square(
                    square_row, 
                    square_col
                )
                
                if revealed and self.grid.is_mined(square_row, square_col):
                    self.show()
                    print("Perdu")
                    return False
            
            elif selected_action == "2":
                self._mark_grid_square(
                    square_row, 
                    square_col)
                
        self.show()
        print("Gagné")
        return True
            
    
    def _ask_player(self, first_turn=False):
        """
        Demande au joueur l'action à effectuer :
        - dévoiler une case
        - marquer une case
        
        ...
        
        Paramètres
        ----------
        first_turn : bool, default=False
            Premier tour de la partie : la case sélectionnée est
            forcément dévoilée.
        
        Retour
        --------
        tuple
            Couple (selected_square, selected_action) où
            selected_square est la liste [ligne, colonne] de la case
            sélectionnée (indexées à partir de 0) et selected_action
            vaut "1" (dévoiler) ou "2" (marquer).
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
    
    def _reveal_grid_square(self, row, col):
        """
        Révèle une case de la grille.
        
        ...
        
        Paramètres
        ----------
        row : int
            Ligne de la case.
        col : int
            Colonne de la case.
        
        Retour
        --------
        bool
            True si la case a été révélée, False sinon.
        """
        return self.grid.reveal_square(row, col)
        
    def _mark_grid_square(self, row, col):
        """
        Marque une case de la grille.
        
        ...
        
        Paramètres
        ----------
        row : int
            Ligne de la case.
        col : int
            Colonne de la case.
        
        Retour
        --------
        bool
            Succès de l'opération.
        """
        return self.grid.mark_square(row, col)
    
    def show(self):
        """
        Affiche la partie dans la console.
        
        ...
        
        Règles
        ------
        - La grille est affichée case par case, ligne par ligne.
        """
        print(self.grid)
        
if __name__ == "__main__":
    level = None
    while level not in Game.LEVELS:
        answer = input("Niveau (1, 2, 3) >>> ")
        if answer.strip() in Game.LEVELS:
            level = int(answer.strip())
        else:
            print("Saisie invalide.\n")
    game = Game(level=level)
    game.launch()
