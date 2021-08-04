import random
import hangman_words
import hangman_art
#Step 1
#def split(word):
#    return [char for char in word]

chosen_word = random.choice(hangman_words.word_list)
#print(f'Pssst, the solution is {chosen_word}.')
#chosen_word_list = split(chosen_word)
#print(chosen_word_list)
lives = 6
display = []
for blank in range (len(chosen_word)):
    display.append("_")

print(f"{' '.join(display)}")
while "_" in display:
    choice_letter = input("Choose a letter: ")
    test_num = 0
    for letter in chosen_word:
        if choice_letter == letter:
            display[test_num] = letter
        test_num += 1
    print(f"{' '.join(display)}")
    if choice_letter not in chosen_word:
        lives -= 1
        print (hangman_art.stages[lives])
    if "_" not in display:
        print ("Humanity restored")
    elif lives == 0:
        print (f"The word was {chosen_word}. \nYou are going to Brazil")
        break

