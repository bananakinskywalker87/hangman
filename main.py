import random
#Step 1
def split(word):
    return [char for char in word]
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = word_list[random.randint(0,2)]
chosen_word_list = split(chosen_word)
#print(chosen_word_list)
choice_letter = input("Choose a letter:")
for letter in chosen_word_list:
    if choice_letter == letter:
        print ("Right")
    else:
        print ("Wrong")

