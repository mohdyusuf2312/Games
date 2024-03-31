import random
from Hangman_words import word_list
from Hangman_stages import stages #Two different ways to import something
import Hangman_logo as logo

print(logo.logo)
chosen_word = random.choice(word_list)

# create list
dash = []
for i in chosen_word:
    dash.append("_")

lives = 6
guess_letter = []
end_of_game = False
while not end_of_game:
    guess = input("Guess a latter: ").lower()
    #If already guessed
    if guess in guess_letter:
        print(f"You've already guessed {guess}")
    #Check letter is present or not
    elif guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, That is not in the word. You lose a life.")
        print(stages[lives])
    else: #fill letter if present
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                dash[i] = guess
    guess_letter.append(guess)
    print(f"{' '.join(dash)}")
    if "_" not in dash:
        end_of_game = True
        print("You Win.")
    elif lives == 0:
        end_of_game = True
        print("You lose.")
        print(f"The word is: {chosen_word}")