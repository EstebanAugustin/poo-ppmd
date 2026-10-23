class Square:
    """
    Instancie une case de la grille
    """
    
    def __init__(self):
        self.is_covered = True
        self.is_mined = False
        self.is_marked = False
        self.hint = 0
    
    def reveal(self):
        """
        Révèle la case
        """
        self.is_covered = False
        return (self.is_mined, self.hint)
        
    def mine(self):
        """
        Mine la case
        """
        self.is_mined = True
        
    def mark(self):
        """
        Marque la case
        """
        self.is_marked = not(self.is_marked)
    
    def show(self):
        """
        Retourne l'affichage de la case
        """
        if self.is_covered:
            if self.is_marked:
                return "\U00002B1B"
            return "\U00002B1C"  # carré
        elif self.is_mined :
            return "# "
        else:
            return str(self.hint) + " "