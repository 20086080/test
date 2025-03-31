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

def check_input(guess_word):
    # Check length of word and if word in permissible list of words
    if len(guess_word) == len(answer):

        # Check against dictionary file provided
        if guess_word in all_words:
            return True
        else:
            print("Unfortunately the word you have selected does "
                  "not match our allocated set of valid words. Please try again.")
            return False
    else:
        print("Unfortunately the game needs a ",len(answer),
              " letter word. Please try again.")
        return False

def analyse_word(guess_word, count_down_temp):
    # Check which alphabets in word are correct & print results
    iteration = 0
    current_list = [0]*(len(guess_word))
    correct_answer = 0
    incorrect_answer = 0
    correct_answer_place = 0

    for guess_iteration in guess_word:
        if guess_iteration == answer[iteration]:
            current_list[iteration] = '2'
            correct_answer_place += 1
        elif guess_iteration in answer:
            current_list[iteration] = '1'
            correct_answer += 1
        else:
            current_list[iteration] = '0'
            incorrect_answer += 1
        iteration += 1

    print("\nYour results are below. You have achieved "
          + str(correct_answer_place)
          + " correct answer(s) '2' in results, \n"
          + str(correct_answer)
          + " correct letter(s) but incorrect place '1' in results,\n "
          + str(incorrect_answer)
          + " incorrect letter(s) '0' in results"
          + " in your #" + str(count_down_temp + 1)
          + " attempt.\n")
    print(list(guess_word))
    print(current_list)


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

    # Check guess word for validity and then each alphabet in word
    if check_input(word):
        analyse_word(word, count_down)
        count_down += 1
