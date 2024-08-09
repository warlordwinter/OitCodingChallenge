class Player():

    def __init__(self):
        self.spots_taken = []
        self.winner = False
    
    def get_spots(self):
        return self.spots_taken
    
    def set_spots(self,spots_taken):
        self.spots_taken = spots_taken
    
    def get_winner(self):
        return self.winner

    def check_win_player(self):
        if ((["A","1"] in self.get_spots()) and (["A","2"] in self.get_spots()) and (["A","3"] in self.get_spots())):
            self.winner = True
            print("True")
        # if (["B","1"] and ["B","2"] and ["B","3"]) in self.spots_taken:
        #     self.winner = True
        #     print("True")
        # if (["C","1"] and ["C","2"] and ["C","3"]) in self.spots_taken:
        #     self.winner = True
        #     print("True")
        # if (["A","1"] and ["B","2"] and ["C","3"]) in self.spots_taken:
        #     self.winner = True
        # if (["C","1"] and ["B","2"] and ["A","3"]) in self.spots_taken:
        #     self.winner = True
        else:
            self.winner = False

