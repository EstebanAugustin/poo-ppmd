class Square:
    """
    Case d'une grille de démineur.
    
    ...
    
    Attributs
    ---------
    is_covered : bool, default=True
        Case couverte ou non.
    is_mined : bool, default=False
        Case minée ou non.
    is_marked : bool, default=False
        Case marquée ou non.
    hint : int, default=0
        Nombre de cases minées voisines.
    
    Méthodes
    --------
    reveal()
        Découvre la case.
    mine()
        Mine la case.
    mark()
        Marque la case.
    __str__()
        Retourne l'affichage console de la case.
    """
    
    def __init__(self):
        self.is_covered = True
        self.is_mined = False
        self.is_marked = False
        self.hint = 0
    
    def reveal(self):
        """
        Change l'état de la case de couvert à découvert.
        
        ...
        
        Règles
        ------
        - Une case ne peut être découverte seulement si elle est
        couverte.
        
        Retour
        --------
        bool
            Succès de l'opération
        """
        
        if self.is_covered:
            self.is_covered = False
            return True
        
        else :
            return False
        
    def mine(self):
        """
        Mine la case.
        
        ...
        
        Retour
        ------
        bool
            Succès de l'opération.
        """
        
        self.is_mined = True
        return True
        
    def mark(self):
        """
        Marque la case.
        
        ...
        
        Règles
        ------
        - Une case peut être marquée ou démarquée seulement si elle est
        couverte.
        
        Retour
        ------
        bool
            Succès de l'opération.
        """
        
        if self.is_covered == True:
            self.is_marked = not(self.is_marked)
            return True
        
        else:
            return False
            
    def __str__(self):
        """
        Retourne l'affichage console de la case.
        
        ...
        
        Règles
        ------
        - Carré blanc si couverte et non marquée.
        - Carré noir si couverte et marquée.
        - "#" si découverte et minée.
        - Indice si découverte et non minée.
        
        Retour
        ------
        str
            Caractère représentant la case.
        """
        if self.is_covered:
            if self.is_marked:
                return "\U00002B1B"
            return "\U00002B1C"  # carré
        elif self.is_mined :
            return "# "
        else:
            return str(self.hint) + " "
        
