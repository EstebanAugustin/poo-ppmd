class Square:
    """
    Instancie une case de la grille
    """
    
    def __init__(self):
        self.is_covered = True
        self.is_mined = True
        self.is_marked = False
        self.hint = 0
    
    def set_is_covered(self, state):
        """
        Change l'état de la case de dé/couvert à dé/couvert
        """
        return
        
    def set_is_mined(self, state):
        """
        Change l'état de la case de déminée à minée
        """
        return
        
    def set_is_marked(self, state):
        """
        Change l'état de la case de non-marquée à marquée
        """
        return
    
    def show(self):
        """
        Retourne l'affichage de la case
        """
        if self.is_covered:
            if self.is_marked:
                return "\U0001F6A9"
            return "\U00002B1B"
        elif self.is_mined :
            return "\U0001F4A3"
        else:
            return "?"