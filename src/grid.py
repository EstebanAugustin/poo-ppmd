import random

from square import Square

class Grid:
    """
    Instancie une grille d'une partie de démineur
    """
    
    def __init__(self, n_rows=5, n_cols=5, n_mines=3):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_mines = n_mines
        self.n_squares_left = n_rows * n_cols
        self.squares = [[Square() for i in range(n_cols)] for i in range(n_rows)]

    def generate(self, excluded_row, excluded_col):
        self.place_mines(excluded_row, excluded_col)
        self.compute_hints()
        self.reveal_square(excluded_row, excluded_col)
        
    def place_mines(self, excluded_row, excluded_col):
        """
        Place les mines sur la grille
        """
        positions = []
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if not (abs(i - excluded_row) <= 1 and abs(j - excluded_col) <= 1):
                    positions.append((i, j))
        
        random.shuffle(positions)
        for i, j in positions[:self.n_mines]:
            self.squares[i][j].mine()
        
    def compute_hints(self):
        """
        Calcule le nombre de mines voisines de chaque case
        """
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                current_square = self.squares[i][j]
                neighbours = self.get_square_neighbours(i, j)
                for k, l in neighbours:
                    square_neighbour = self.squares[k][l]
                    if square_neighbour.is_mined == True:
                        current_square.hint += 1
        
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
        print(string)
        
    def reveal_square(self, row, col):
            """
            Révèle une case et propage récursivement la découverte aux voisins 
            si la case n'est pas minée et que son indice est 0.
            """
            current_square = self.squares[row][col]
            
            if not current_square.is_covered:
                return False
                
            square_is_mined, square_hint = current_square.reveal()
            self.n_squares_left -= 1
            
            if square_is_mined:
                return True
                
            if square_hint == 0:
                for neighbour_row, neighbour_col in self.get_square_neighbours(row, col):
                    self.reveal_square(neighbour_row, neighbour_col)
                    
            return False
    
    def count_squares(self):
        return self.n_squares_left - self.n_mines

        
    def mark_square(self, row, col):
        """
        Marque une case
        """
        self.squares[row][col].mark()
        