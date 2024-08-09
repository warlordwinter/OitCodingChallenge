class Player():

    def __init__(self):
        self.spots_taken = []
    
    def get_spots(self):
        return self.spots_taken
    
    def set_spots(self,spots_taken):
        self.spots_taken = spots_taken
        
