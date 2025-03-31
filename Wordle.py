#20086080 Monisha Sikka 31-03-2025

import random

def get_user_input():
    # Prompt for User guess word
    prompt = (("\nAttempt "
               + str(count_down + 1)
               + " of "
               + str(number_tries)
               + " - Please enter your ")
              + str(len(answer))
              + " letter word or Q to quit: ")
    return input(prompt).upper()

def get_answer():
    # Get random guess word answer
    return list(random.choice(answer_list).upper())

def play_again():
    # Check if user wants to play again
    new_game = ""
    while new_game !="Y" and new_game !="N":
            new_game = input("\nPlay again Y / N ").upper()
            if new_game == "N" :
                return False
            elif new_game == "Y" :
                return True

count_down = 0
number_tries = 6

# Open target file and make a list of all possible guess answers
answer_list = []
all_words = []

target_file = open("./target_words.txt","r")
for line in target_file:
    answer_list.append(line.strip())
target_file.close()

valid_word_file = open("./all_words.txt","r")
for line in valid_word_file:
    all_words.append(line.strip().upper())
valid_word_file.close()

# Get random answer to puzzle
answer = get_answer()
print(answer)

while count_down < number_tries :
    word = get_user_input()

    # If User decides to quit the games
    if word == "Q":
        print("The answer you were guessing is " + "".join(answer)
              + "\nSorry to see you go. Come back soon!!!")
        break

    # If word is correctly guessed
    if answer == list(word):
        print("\nDrum Rolls!!! You have guessed the correct word "
              + word + " in " + str(count_down + 1) + " attempt(s).\n"
                                                      "You are a champion!!!")
        if play_again():
            count_down = 0
            answer = get_answer()
            print(answer)
            continue
        else:
            break

    count_down += 1