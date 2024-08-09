class Game():
    """This is the game object that holds the Tic Tac Toe game."""
    def __init__(self, current_player, board = None):
        self.current_player = current_player
        self.board = board
    
    def get_current_player(self):
        """Gets the current player"""
        return self.current_player
    
    def set_current_player(self, player):
        """Sets the current player"""
        self.current_player = player