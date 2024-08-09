import game as game

def main():
    # new_game = game.Game("john", "doe")
    # new_game.set_current_player("jane")
    # print(new_game.get_current_player())
    # print("Hello World!")
    print("Welcome to Tic Tac Toe!")
    starting_player = input("Who will go first? Player or Computer? ex: 'Player' or 'Computer' ")
    new_game = game.Game(starting_player)
    new_game.make_move()

if __name__ == "__main__":
    main()