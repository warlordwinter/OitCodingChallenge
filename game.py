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
        self.tie_game = False

    def get_tie(self):
        """Finds if there is a tie game"""
        return self.tie_game
    
    def set_tie(self):
        self.tie_game = True
    
    def get_current_player(self):
        """Gets the current player"""
        return self.current_player
    
    def get_game_over(self):
        return self.game_over
    
    def set_game_over(self,game_over):
        self.game_over = game_over
    
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
        current_row = legal_moves[row]
        changed_board = current_row[:column]+[symbol]+current_row[column+1:]
        legal_moves = legal_moves[:row]+[changed_board]+legal_moves[row+1:]
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
            potential_winner = self.get_player()
            potential_winner.check_win_player()
            if potential_winner.get_winner() == True:
                self.set_game_over(True)
        else:
            potential_winner = self.get_player()
            potential_winner.get_winner()

    def check_tie(self):
        if len(self.get_available_moves()) == 0:
            self.set_game_over(True)
            self.set_tie_game()


    
    def make_move(self):
        """Makes a move on the board"""
        if self.current_player == "Player":
            row_cordinate = input("Insert the Row Cordinate ex: A,B,C: " )
            column_cordinate = input("Insert the Column Cordinate ex: 1,2,3: " )
            cordinate_pair = [row_cordinate,column_cordinate]
            moves = self.get_available_moves()
            if cordinate_pair in moves:

                player = self.get_player()
                spots_taken = self.player.get_spots()
                spots_taken.insert(0,cordinate_pair)

                player.set_spots(spots_taken)

                moves.remove([row_cordinate,column_cordinate])
                row_cordinate = self.convert_letters_to_nums(row_cordinate)
                self.change_board(row_cordinate,int(column_cordinate),symbol = "[X]")
                self.check_win()
                self.check_tie()
                if self.get_game_over() ==True:
                    return True
                self.current_player ="Computer"

        else:
            moves =self.get_available_moves() #The computer will randomly grab a move and store it in it's taken moves list
            index = randint(0,len(moves))
            chosen_move = moves[index-1]
            row_cordinate = chosen_move[0]
            column_cordinate = chosen_move[1]
            moves.remove([row_cordinate,column_cordinate])
            row_cordinate=self.convert_letters_to_nums(row_cordinate)
            self.change_board(row_cordinate,int(column_cordinate),symbol = "[O]")
            computer = self.get_computer()
            spots_taken = computer.get_spots()
            cordinate_pair= [row_cordinate,column_cordinate]
            spots_taken.insert(0,cordinate_pair)
            self.check_win()
            self.check_tie()
            self.current_player = "Player"



            
            


