import game as game

def main():
    # new_game = game.Game("john", "doe")
    # new_game.set_current_player("jane")
    # print(new_game.get_current_player())
    # print("Hello World!")
    print("Welcome to Tic Tac Toe!")
    starting_player = input("Who will go first? Player or Computer? ex: 'Player' or 'Computer' ")
    new_game = game.Game(starting_player)
    while new_game.game_over == False:
        print(new_game.get_board())
        new_game.make_move()
    start_over = input("Thanks for playing! Want to play again? ex: Yes/No")
    if start_over == "Yes":
        main()


if __name__ == "__main__":
    main()