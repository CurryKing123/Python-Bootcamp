import random

word_list = ["dragon", "tower", "warrior", "mage"]
random_word = random.choice(word_list)

#Make a list of blanks from the appended list
blank_list = ""
for int in range(len(random_word)):
    blank_list += "_"

guesses = 5
win_condition = False

# def user_guess():
#     guess = input("Guess a letter: ").lower()
#     for letter in random_word:
#         if letter == guess:
#             display += letter
#         else:
#             display += "_"



print(f"Hangman Game: Your word has {len(random_word)} letters")

correct_letters = []
incorrect_letters =[]

while guesses > 0 or win_condition == True:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in random_word:
        if guess not in incorrect_letters:
            incorrect_letters += guess
            guesses -= 1

    print(incorrect_letters)
    
    #user_guess()
    print(display)
    print(f"You have {guesses} guesses left")

    if "_" not in display:
        win_condition = True
        print("You Win")

print("Game Over")