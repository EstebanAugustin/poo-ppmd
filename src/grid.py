import random

from square import Square

class Grid:
    """
    Grille de démineur.
    
    ...
    
    Attributs
    ---------
    _n_rows : int, default=5
        Nombre de lignes de la grille.
    _n_cols : int, default=5
        Nombre de colonnes de la grille.
    _n_mines : int, default=3
        Nombre de cases minées dans la grille.
    _n_squares_left : int
        Nombre de cases restantes couvertes.
    _squares : Square[]
        Tableau 2D des cases de la grille.
        
    Méthodes
    --------
    place_mines(excluded_row, excluded_col)
        Place les mines sur la grille.
    compute_hints()
        Calcules les indices de chaque case.
    _get_square_neighbours(row, col)
        Retourne les cases voisines d'une case.
    _is_in_grid(row, col)
        Vérifie que les coordonnées sont dans la grille.
    __str__()
        Retourne l'affichage console de la grille.
    reveal_square(row, col)
        Révèle une case et propage la découverte aux voisins.
    is_mined(row, col)
        Indique si une case est minée.
    count_squares()
        Retourne le nombre de cases restantes.
    mark_square(row, col)
        Marque une case.
    
    """
    
    def __init__(self, n_rows=10, n_cols=10, n_mines=10):
        if n_rows <= 0 or n_cols <= 0:
            raise ValueError("n_rows et n_cols doivent être strictement positifs.")
        if n_mines < 0 or n_mines >= n_rows * n_cols:
            raise ValueError("n_mines doit être entre 0 et n_rows * n_cols - 1.")
        self._n_rows = n_rows
        self._n_cols = n_cols
        self._n_mines = n_mines
        self._n_squares_left = n_rows * n_cols
        self._squares = [
            [Square() for _ in range(n_cols)] for _ in range(n_rows)
        ]
    
    @property
    def n_rows(self):
        return self._n_rows
    
    @property
    def n_cols(self):
        return self._n_cols
    
    @property
    def n_mines(self):
        return self._n_mines
    
    @property
    def n_squares_left(self):
        return self._n_squares_left
    
    @property
    def squares(self):
        return self._squares
            
    def place_mines(self, excluded_row, excluded_col):
        """
        Place les mines selon l'algorithme de Fisher-Yates
        
        ...
        
        Algorithme
        ----------
        - Créer la liste contenant toutes les cases de la grille
        - Pour i allant de n-1 à 1:
            - Choisir k aléatoire entre 0 et i
            - Échanger la case i avec la case k dans la liste
        - Les M premières cases de la liste sont les cases minées
        
        Paramètres
        ----------
        excluded_row : int
            Ligne de la case cliquée par le joueur.
        excluded_col : int
            Colonne de la case cliquée par le joueur.
        """
        squares = []
        for i in range(self._n_rows):
            for j in range(self._n_cols):
                if abs(i - excluded_row) > 1 and abs(j - excluded_col) > 1:
                    squares.append((i,j))
         
        for i in range(len(squares)-1, 0, -1):
            k = random.randint(0, i)
            tmp = squares[i]
            squares[i] = squares[k]
            squares[k] = tmp
        
        for _ in range(self._n_mines):
            i, j = squares[_]
            self._squares[i][j].mine()
        
        
    def compute_hints(self):
        """
        Calcule le nombre de cases minées adjacentes à chaque case.
        
        ...
        
        Règles
        ------
        - Le résultat est stocké dans l'attribut hint de chaque case.
        """
        for i in range(self._n_rows):
            for j in range(self._n_cols):
                current_square = self._squares[i][j]
                neighbours = self._get_square_neighbours(i, j)
                
                for k, l in neighbours:
                    square_neighbour = self._squares[k][l]
                    
                    if square_neighbour.is_mined == True:
                        current_square.increment_hint()
        
    def _is_in_grid(self, row, col):
        """
        Vérifie que les coordonnées sont dans la grille.
        
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
            True si la case est dans la grille, False sinon.
        """
        return 0 <= row < self._n_rows and 0 <= col < self._n_cols
    
    def _get_square_neighbours(self, row, col):
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
            row_in_grid = (row >= 0 and row < self._n_rows)
            col_in_grid = (col >= 0 and col < self._n_cols)
            
            if row_in_grid and col_in_grid:
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
        for i in range(self._n_rows):
            for j in range(self._n_cols):
                string += str(self._squares[i][j])
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
        indice est 0 et qu'elles ne sont pas minées.
        - Si les coordonnées sont hors de la grille, rien ne se passe.
        
        Retour
        --------
        bool
            True si la case a été révélée, False sinon.
        """
        if not self._is_in_grid(row, col):
            return False
            
        current_square = self._squares[row][col]
        
        if not current_square.is_covered:
            return False
            
        current_square.reveal()
        self._n_squares_left -= 1
        
        if current_square.hint == 0 and not current_square.is_mined:
            neighbours = self._get_square_neighbours(row, col)
            
            for neighbour_row, neighbour_col in neighbours:
                self.reveal_square(neighbour_row, neighbour_col)
                
        return True
    
    def is_mined(self, row, col):
        """
        Indique si une case est minée.
        
        ...
        
        Paramètres
        ----------
        row : int
            Ligne de la case.
        col : int
            Colonne de la case.
        
        Règles
        ------
        - Si les coordonnées sont hors de la grille, retourne False.
        
        Retour
        --------
        bool
            True si la case est minée, False sinon.
        """
        if not self._is_in_grid(row, col):
            return False
            
        return self._squares[row][col].is_mined
    
    def count_squares(self):
        """
        Retourne le nombre de cases restantes.
        
        ...
        
        Retour
        --------
        int
            Nombre de cases couvertes non minées restantes.
        """
        return self._n_squares_left - self._n_mines

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
        
        Règles
        ------
        - Si les coordonnées sont hors de la grille, rien ne se passe.
        
        Retour
        --------
        bool
            Succès de l'opération.
        """
        if not self._is_in_grid(row, col):
            return False
            
        return self._squares[row][col].mark()
        
