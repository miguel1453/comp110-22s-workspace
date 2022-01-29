"""EX01 - Chardle - A cute step toward Worlde."""

__author__ = "730472629"

instance_count = 0
user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: word must contain five characters.")
    exit()
letter_to_check: str = input("Enter a single character: ")
if len(letter_to_check) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter_to_check + " in " + user_word)

if letter_to_check == user_word[0]:
    print(letter_to_check + " found at index 0")
    instance_count = instance_count + 1
if letter_to_check == user_word[1]:
    print(letter_to_check + " found at index 1")
    instance_count = instance_count + 1
if letter_to_check == user_word[2]:
    print(letter_to_check + " found at index 2")
    instance_count = instance_count + 1
if letter_to_check == user_word[3]:
    print(letter_to_check + " found at index 3")
    instance_count = instance_count + 1
if letter_to_check == user_word[4]:
    print(letter_to_check + " found at index 4")
    instance_count = instance_count + 1
if instance_count == 0:
    print("No instances of " + letter_to_check + " found in " + user_word)
if instance_count == 1:
    print(instance_count, "instance of " + letter_to_check + " found in " + user_word)
else: 
    print(instance_count, "instances of " + letter_to_check + " found in " + user_word)
        
