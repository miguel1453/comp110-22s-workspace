"""One shot wordle exercise."""
__author__ = "730472629"

"""initialzing variables"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

has_letter = False
idx = 0
i = 0 
block: str = ""
secret_word = "python"

"""input: asks user for their guess and checks to see if is the correct lenght"""
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(guess) != len(secret_word): 
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

"""main loop that assigns the color of box for the output"""
while i != len(secret_word):
    if guess[i] == secret_word[i]:
        block = block + GREEN_BOX
    else:
        """loop to see if guess[i] is ANYWHERE in the secret_word"""
        idx = 0
        has_letter = False
        while has_letter is False and idx < len(secret_word):
            if guess[i] == secret_word[idx]:
                has_letter = True
            idx = idx + 1
        if has_letter is True:
            block = block + YELLOW_BOX
        else:
            block = block + WHITE_BOX
    i = i + 1

"""output to user"""
print(block)
if guess == secret_word:
    print("Woo! You got it!\n")
else:
    print("Not quite. Play again soon!\n")