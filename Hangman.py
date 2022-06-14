import random
import Hangman_word
from Hangman_art import logo, stages



chosen_word = random.choice(Hangman_word.word_list)
print(logo)
display = []

for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False
lives = 6
while not end_of_game:
    guss_letter = input("Guss the letter: ").lower()
    if guss_letter in display:
        print("You have already guessed this Character")
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guss_letter:
            display[letter] = guss_letter

    print(display)
    if guss_letter not in chosen_word:
        print(stages[lives])
        print(f"you have chosen {guss_letter}. That is not in the word. You lose 1 Life:(")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(stages[lives])
            print("You lose")

    elif "_" not in display:
        end_of_game = True
        print("You win")