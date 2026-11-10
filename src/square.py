class Square:
    """
    Case d'une grille de démineur.
    
    ...
    
    Attributs
    ---------
    _is_covered : bool, default=True
        Case couverte ou non.
    _is_mined : bool, default=False
        Case minée ou non.
    _is_marked : bool, default=False
        Case marquée ou non.
    _hint : int, default=0
        Nombre de cases minées voisines.
    
    Méthodes
    --------
    reveal()
        Découvre la case.
    mine()
        Mine la case.
    mark()
        Marque la case.
    increment_hint()
        Incrémente l'indice de la case.
    __str__()
        Retourne l'affichage console de la case.
    """
    
    def __init__(self):
        self._is_covered = True
        self._is_mined = False
        self._is_marked = False
        self._hint = 0
    
    @property
    def is_covered(self):
        return self._is_covered
    
    @property
    def is_mined(self):
        return self._is_mined
    
    @property
    def is_marked(self):
        return self._is_marked
    
    @property
    def hint(self):
        return self._hint
    
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
        
        if self._is_covered:
            self._is_covered = False
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
        
        self._is_mined = True
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
        --------
        bool
            Succès de l'opération.
        """
        
        if self._is_covered == True:
            self._is_marked = not(self._is_marked)
            return True
        
        else:
            return False
            
    def increment_hint(self):
        """
        Incrémente l'indice de la case de 1.
        
        ...
        
        Retour
        ------
        int
            Nouvel indice de la case.
        """
        self._hint += 1
        return self._hint
        
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
        --------
        str
            Caractère représentant la case.
        """
        if self._is_covered:
            if self._is_marked:
                return "\U00002B1B"
            return "\U00002B1C"  # carré
        elif self._is_mined :
            return "# "
        else:
            return str(self._hint) + " "
        
