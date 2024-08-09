import game as game

def main():
    # new_game = game.Game("john", "doe")
    # new_game.set_current_player("jane")
    # print(new_game.get_current_player())
    # print("Hello World!")
    print("Welcome to Tic Tac Toe!")
    starting_player = input("Who will go first? Player or Computer? ex: 'Player' or 'Computer' ")
    new_game = game.Game(starting_player)
    letters = ["A","B","C"]
    while new_game.game_over == False:
        if(new_game.get_current_player() == "Player"):
            print("   1     2     3")
            for i in range(len(new_game.get_board())):
                print(letters[i]+str(new_game.get_board()[i]))
        if ((new_game.make_move() == True) and (new_game.get_tie != True)):
            print(new_game.get_current_player() + " Is the Winner")
            break
        if(new_game.get_tie == True):
            print("Tie Game!")
            break
    start_over = input("Thanks for Playing! Want to play again? ex: Yes/No ")
    if start_over == "Yes":
        main()
    else:
        print("Come Again Soon!")


if __name__ == "__main__":
    main()