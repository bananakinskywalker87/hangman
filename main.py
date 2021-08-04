import random
#Step 1
#def split(word):
#    return [char for char in word]
word_list = ["aardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0,2)]
print(f'Pssst, the solution is {chosen_word}.')
#chosen_word_list = split(chosen_word)
#print(chosen_word_list)

display = []
for blank in range (len(chosen_word)):
    display.append("_")

#print (display)
choice_letter = input("Choose a letter:")
test_num = 0
for letter in chosen_word:
    if choice_letter == letter:
        display[test_num] = letter
    test_num += 1
print (display)

