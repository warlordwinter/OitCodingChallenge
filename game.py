from random import randint
import player as player
class Game():
    """This is the game object that holds the Tic Tac Toe game."""
    def __init__(self, current_player, board = None):
        self.current_player = current_player
        self.board = [["[]","[]","[]"],["[]","[]","[]"],["[]","[]","[]"]]
        self.avaliable_moves = [["A","1"],["A","2"],["A","3"],["B","1"],["B","2"], ["B","3"], ["C","1"],["C","2"],["C","3"]]
        self.player = player.Player()
        self.computer = player.Player()
        self.game_over = False
    
    def get_current_player(self):
        """Gets the current player"""
        return self.current_player
    
    def get_game_over(self):
        return self.get_game_over
    
    def set_current_player(self, player):
        """Sets the current player"""
        self.current_player = player
    
    def get_available_moves(self):
        """Gets the available moves"""
        return self.avaliable_moves
    
    def get_board(self):
        """Gets the Board"""
        return self.board
    
    def set_board(self,board):
        self.board = board

    def get_player(self):
        return self.player
    
    def get_computer(self):
        return self.computer
    
    def change_board(self,row,column,symbol):
        """When a player makes a legal move this function changes the board to reflect this"""
        legal_moves = self.get_board()
        row = row-1
        column = column-1
        # print(legal_moves)
        current_row = legal_moves[row]
        # print(current_row)
        changed_board = current_row[:column]+[symbol]+current_row[column+1:]
        # print(changed_board)
        legal_moves = legal_moves[:row]+[changed_board]+legal_moves[row+1:]
        # print(legal_moves)
        self.set_board(legal_moves)


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

    def check_win(self):
        if self.current_player == "Player":
            potential_winner = self.get_current_player()
            potential_winner.get_winner()


    
    def make_move(self):
        """Makes a move on the board"""
        if self.current_player == "Player":
            row_cordinate = input("Insert the Row Cordinate ex: A,B,C: " )
            column_cordinate = input("Insert the Column Cordinate ex: 1,2,3: " )
            cordinate_pair = [row_cordinate,column_cordinate]
            moves = self.get_available_moves()
            if cordinate_pair in moves:
                #print("True")
                player = self.get_player()
                spots_taken = self.player.get_spots()
                spots_taken.insert(0,cordinate_pair)
                # print(spots_taken)
                player.set_spots(spots_taken)
                # print(player.get_spots())
                moves.remove([row_cordinate,column_cordinate])
                # print(moves)
                row_cordinate = self.convert_letters_to_nums(row_cordinate)
                self.change_board(row_cordinate,int(column_cordinate),symbol = "[X]")
                self.current_player ="Computer"
        else:
            moves =self.get_available_moves() #The computer will randomly grab a move

            randint(0,len(moves))


            
            


