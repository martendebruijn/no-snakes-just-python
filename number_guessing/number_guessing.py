"""Terminal number guessing game.

This script allows the user to play a game where the player needs to guess a secret
number.
"""

import sys
import random


def ask_for_int(question: str) -> int | None:
    """Ask for input that must be an integer.

    Parameters
    ----------
    question : str
        The question being asked.

    Returns
    -------
    int
        The inputted integer.

    Raises
    ------
    ValueError
        If inputted value is not an integer.
    """
    answer = input(f"{question}\n")
    try:
        return int(answer)
    except ValueError:
        print("\nPlease enter an integer.\r")
        ask_for_int("Please try again.")


def change_settings(min: int, max: int) -> tuple[int, int] | None:
    """Ask to change the range for the game.

    Parameters
    ----------
    min : int
        The minimum value.
    max : int
        The maximum value.

    Returns
    -------
    tuple of int
        (min, max)
    """
    answer = input(
        f"\nThe default is a target number between {min} and {max}, inclusive.\nDo you like to change these? (n/y)\n"
    )
    if answer.lower() == "n":
        minmax = (min, max)
    elif answer.lower() == "y":
        minmax = change_min_max()
    else:
        print("Please enter y or n\n")
        change_settings()
    return minmax


def change_min_max() -> tuple[int | None, int | None] | None:
    """Change the min and max values for the game.

    Returns
    -------
    tuple of int
        (min, max)
    """
    min = ask_for_int("\nPlease enter a minimum value:")
    max = ask_for_int("\nPlease enter a maximum value:")
    if max <= min:
        print(
            "The maximum value must be higher than the minimum value.\rPlease enter the minimum and maximum values again."
        )
        change_min_max()
    else:
        return (min, max)


def start_game(options: dict[int, int] = {"min": 1, "max": 100}):
    """Start a game

    Parameters
    ----------
    options : dict, optional, default: { "min": 1, "max": 100 }
        The default range of the game.

    Returns
    -------
    function
        The function that controls making a guess.
    """
    min, max = change_settings(min=options["min"], max=options["max"])
    target = random.randint(min, max)

    def make_guess(round: int = 1) -> None:
        """Make a guess.

        Parameters
        ----------
        round : int, optional, default: 1
            The current round number

        Raises
        ------
        ValueError
            If inputted value is not an integer.
        """
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


def ask_play_again() -> None:
    """Ask player to play again."""
    new_game = input("\nDo you want to play again? (n/y)\n")
    if new_game.lower() == "y":
        start_game()()
    elif new_game.lower() == "n":
        sys.exit()
    else:
        ask_play_again()


start_game()()
