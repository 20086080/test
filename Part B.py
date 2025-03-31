#20086080 Monisha Sikka 20-03-2025

def score_guess(guess_word, target_word):
    """This function accepts 2 parameters which are string, namely
    guess_word & target_word. Guess_word is a word selected by
    the user to compare to target_word. If the guess_word matches
    the target_word, then a score of 2 for each letter in guess_word
    is returned. A score of 1 is calculated for every letter in
    guess_word which exists in target_word though not in the same
    position within the word. A total score of guess_word is returned by
    this function.
    :param guess_word:
    :param target_word:
    :return: score of guess_word
    """

    # Create empty list of score values
    score = [0]*(len(target_word))
    interation = 0

    # Iterate through every letter in guess_word
    for guess_interation in guess_word:
        if guess_interation == target_word[interation]:
            score[interation] = 2
        elif guess_interation in target_word:
            score[interation] = 1
        interation += 1
    return score

answer_list = []
all_words = []

target_file = open("./target_words.txt","r")
for line in target_file:
    answer_list.append(line.strip())
target_file.close()
length = len(answer_list)
print("First 5 Target Words : ", answer_list[0:5])
print("Last 5 Target Words : ", answer_list[length-6:length-1])


valid_word_file = open("./all_words.txt","r")
for line in valid_word_file:
    all_words.append(line.strip())
valid_word_file.close()
length = len(all_words)
print("First 5 words from All words : ", all_words[0:5])
print("Last 5 words from All words : ", all_words[length-6:length-1])

#test arrange guess word, target word
guess = "world"
target = "hello"

#act call score guess to calculate score
score_of_word = score_guess(guess, target)

#Assert
print("Guess : ", guess)
print("Target : ", target)
print("Expected : [0 ,1 ,0 ,2 ,0]")
print("Got : ", score_of_word)