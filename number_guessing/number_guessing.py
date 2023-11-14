import sys
import random


def ask_for_int(question):
    answer = input(f"{question}\n")
    try:
        return int(answer)
    except ValueError:
        print("\nPlease enter an integer.\r")
        ask_for_int("Please try again.")


def change_settings(min, max):
    answer = input(
        f"\nThe default is a target number between {min} and {max}, inclusive.\nDo you like to change these? (n/y)\n"
    )
    if answer.lower() == "n":
        minmax = [min, max]
    elif answer.lower() == "y":
        minmax = change_min_max()
    else:
        print("Please enter y or n\n")
        change_settings()
    return minmax


def change_min_max():
    min = ask_for_int("\nPlease enter a minimum value:")
    max = ask_for_int("\nPlease enter a maximum value:")
    if max <= min:
        print(
            "The maximum value must be higher than the minimum value.\rPlease enter the minimum and maximum values again."
        )
        change_min_max()
    else:
        return [min, max]


def start_game(options={"min": 1, "max": 100}):
    print(options["min"])
    min, max = change_settings(min=options["min"], max=options["max"])
    target = random.randint(min, max)

    def make_guess(round=1):
        print(f"\nRound: {round}")
        guess = input("Please enter your guess:\n")

        try:
            guess = int(guess)
            if guess == target:
                print(f"\nYou win!\nYou have won in {round} rounds!")
                ask_play_again()
            else:
                print("\nToo small!\n" if guess < target else "\nToo Big!\n")
                round += 1
                make_guess(round)

        except ValueError:
            print("Must be an integer.")
            make_guess(round)

    return make_guess


def ask_play_again():
    new_game = input("\nDo you want to play again? (n/y)\n")
    if new_game.lower() == "y":
        start_game()()
    elif new_game.lower() == "n":
        sys.exit()
    else:
        ask_play_again()


start_game()()
