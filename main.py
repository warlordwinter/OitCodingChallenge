import game as game

def main():
    new_game = game.Game("john", "doe")
    new_game.set_current_player("jane")
    print(new_game.get_current_player())
    print("Hello World!")

if __name__ == "__main__":
    main()