class Game():
    """This is the game object that holds the Tic Tac Toe game."""
    def __init__(self, current_player, board = None):
        self.current_player = current_player
        self.board = [["[]","[]","[]"],["[]","[]","[]"],["[]","[]","[]"]]
        self.avaliable_moves = [["A","1"],["A","2"],["A","3"],["B","1"],["B","2"], ["B","3"], ["C","1"],["C","2"],["C","3"]]
    
    def get_current_player(self):
        """Gets the current player"""
        return self.current_player
    
    def set_current_player(self, player):
        """Sets the current player"""
        self.current_player = player
    
    def get_available_moves(self):
        """Gets the available moves"""
        return self.avaliable_moves
    
    def get_board(self):
        """Gets the Board"""
        return self.board
    
    def change_board(self,row,column,symbol):
        """When a player makes a legal move this function changes the board to reflect this"""
        legal_moves = self.get_board()
        print(legal_moves)
        current_row = legal_moves[row]
        print(current_row)
        changed_board = current_row[:column]+[symbol]+current_row[column+1:]
        print(changed_board)

    def convert_letters_to_nums(self, row):
        """Converts ABC to 123"""
        if row == "A":
            return 1
        if row == "B":
            return 2
        if row == "C":
            return 3
        else:
            print("Error with Letter Conversion")



    
    def make_move(self):
        """Makes a move on the board"""
        if self.current_player == "Player":
            row_cordinate = input("Insert the Row Cordinate ex: A,B,C: " )
            column_cordinate = input("Insert the Column Cordinate ex: 1,2,3: " )
            cordinate_pair = [row_cordinate,column_cordinate]
            moves = self.get_available_moves()
            if cordinate_pair in moves:
                #print("True")
                row_cordinate = self.convert_letters_to_nums(row_cordinate)
                self.change_board(row_cordinate,int(column_cordinate),symbol = "[X]")

