#20086080 Monisha Sikka 31-03-2025

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

answer = "hello"

count_down = 0
number_tries = 6

while count_down < number_tries :
    word = get_user_input()

    # If User decides to quit the games
    if word == "Q":
        print("The answer you were guessing is " + "".join(answer)
              + "\nSorry to see you go. Come back soon!!!")
        break

    count_down += 1