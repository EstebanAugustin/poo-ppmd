import random

from square import Square

class Grid:
    """
    Grille de démineur.
    
    ...
    
    Attributs
    ---------
    n_rows : int, default=5
        Nombre de lignes de la grille.
    n_cols : int, default=5
        Nombre de colonnes de la grille.
    n_mines : int, default=3
        Nombre de cases minées dans la grille.
    n_squares_left : int
        Nombre de cases restantes couvertes.
    squares : Square[]
        Tableau 2D des cases de la grille.
        
    Méthodes
    --------
    place_mines(excluded_row, excluded_col)
        Place les mines sur la grille.
    compute_hints()
        Calcules les indices de chaque case.
    get_square_neighbours(row, col)
        Retourne les cases voisines d'une case.
    __str__()
        Retourne l'affichage console de la grille.
    reveal_square(row, col)
        Révèle une case et propage la découverte aux voisins.
    count_squares()
        Retourne le nombre de cases restantes.
    mark_square(row, col)
        Marque une case.
    
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
        Place les mines sur la grille.
        
        ...
        
        Règles
        ------
        - Les mines ne sont placées ni sur la case cliquée par le
        joueur ni sur ses cases voisines.
        
        Paramètres
        ----------
        excluded_row : int
            Ligne de la case cliquée par le joueur.
        excluded_col : int
            Colonne de la case cliquée par le joueur.
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
        Calcule le nombre de cases minées adjacentes à chaque case.
        
        ...
        
        Règles
        ------
        - Le résultat est stocké dans l'attribut hint de chaque case.
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
                
    def __str__(self):
        """
        Retourne l'affichage console de la grille.
        
        ...
        
        Retour
        --------
        str
            Chaîne représentant la grille, case par case et ligne par
            ligne.
        """
        string = ""
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                string += str(self.squares[i][j])
                string += " "
            string += "\n"
            
        return string
        
    def reveal_square(self, row, col):
        """
        Révèle une case et propage la découverte aux voisins si la case
        n'est pas minée et que son indice est 0.
        
        ...
        
        Paramètres
        ----------
        row : int
            Ligne de la case.
        col : int
            Colonne de la case.
        
        Règles
        ------
        - Une case déjà découverte n'est pas révélée à nouveau.
        - La découverte se propage aux cases voisines tant que leur
        indice est 0.
        
        Retour
        --------
        bool
            True si la case révélée est minée, False sinon.
        """
        current_square = self.squares[row][col]
        
        if not current_square.is_covered:
            return False
            
        current_square.reveal()
        self.n_squares_left -= 1
        
        if current_square.is_mined:
            return True
            
        if current_square.hint == 0:
            neighbours = self.get_square_neighbours(row, col)
            
            for neighbour_row, neighbour_col in neighbours:
                self.reveal_square(neighbour_row, neighbour_col)
                
        return False
    
    def count_squares(self):
        return self.n_squares_left - self.n_mines
        """
        Retourne les cases voisines d'une case.
        
        ...
        
        Paramètres
        ----------
        row : int
            Ligne de la case.
        col : int
            Colonne de la case.
        
        Retour
        --------
        list of tuple of int
            Coordonnées (ligne, colonne) des cases voisines situées
            dans la grille.
        """

        
    def mark_square(self, row, col):
        """
        Marque une case.
        
        ...
        
        Paramètres
        ----------
        row : int
            Ligne de la case.
        col : int
            Colonne de la case.
        """
        self.squares[row][col].mark()
                """
        Retourne le nombre de cases restantes.
        
        ...
        
        Retour
        --------
        int
            Nombre de cases couvertes non minées restantes.
        """
