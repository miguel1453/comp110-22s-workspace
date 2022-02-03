"""Strcutured wordle exercise"""
__author__ = "730472629"


def main() -> None:
    """The entrypoint of the program and main game loop"""
    secret: str = "codes"
    turns: int = 6
    i: int = 1
    guess: str = ""
    while i <= 6 and guess != secret:
        print(f"=== Turn {i}/{turns} ===")
        guess = input_guess(len(secret))
        box_output: str = emojified(guess, secret)
        print(box_output)
        i += 1
    if guess == secret:
        print(f"You won in {i}/{turns} turns!")
    else:
        print(f"X/{turns} - Sorry, try again tomorrow!")


def input_guess(expected_length: int) -> str:
    """checks the length of the guess"""
    guess: str = str(input(f"Enter a {expected_length} letter word: "))
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} characters! Try again: ")
    return guess


def emojified(guess: str, secret) -> str:
    """assings the color of the box for the user output"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    box_output: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            box_output += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            box_output += YELLOW_BOX
        else:
            box_output += WHITE_BOX
        i += 1
    return box_output


def contains_char(secret: str, letter_to_check: str) -> bool:
    """checks input word to see if characters match up anywhere in secret"""
    assert len(letter_to_check) == 1
    i: int = 0
    while i < len(secret):
        if secret[i] == letter_to_check:
            return True
        i += 1
    return False


if __name__ == "__main__":
    main()