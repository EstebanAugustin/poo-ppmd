from square import Square

class Grid:
    """
    Instancie une grille d'une partie de démineur
    """
    
    def __init__(self, n_rows=10, n_cols=10, n_mines=10):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_mines = n_mines
        self.squares = [[Square() for i in range(n_cols)] for i in range(n_rows)]
        
    def place_mines(self):
        """
        Place les mines sur la grille
        """
        return
        
    def compute_hints(self):
        """
        Calcule le nombre de mines voisines de chaque case
        """
        return
    def get_square_neighbours(self, row, col):
        neighbours = [
            (row-1, col-1),
            (row-1, col),
            (row-1, col+1),
            (row, col-1),
            (row, col+1),
            (row+1, col-1),
            (row+1, col),
            (row+1, col+1)
        ]
        
        valid_neighbours = []
        
        for i, (row, col) in enumerate(neighbours) :
            if row >= 0 and col >= 0 and row < self.n_rows and col < self.n_cols:
                valid_neighbours.append((row, col))
                
        return valid_neighbours
                
        
    def show(self):
        """
        Retourne l'affichage de la grille
        """
        string = ""
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                string += self.squares[i][j].show()
                string += " "
            string += "\n"
        return string
        
    def reveal_square(self):
        """
        Révèle une case
        """
        return
        
    def mark_square(self):
        """
        Marque une case
        """
        return
        