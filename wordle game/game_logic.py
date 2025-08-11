# task 6.1: backend
import random
def guess_word():

    def load_words(words):
        with open(words, "r") as f:
            words = [word.strip().lower() for word in f if len(word.strip()) == 5]
        
        return words, set(words)
    words, word_set = load_words("words.txt")
    selected_word = random.choice (words)
    
    user_guess = input("guess the word: ")
    for n in range(6):
        if user_guess == selected_word:
            print ("Congrats! you've guessed the right word in " + str(n+1) + " attempts")
            break
        else:
            print ("That's not correct please try again")
            user_guess = input("guess the word: ")
            continue
    else:
        print("you're out of attempts! The word was " + selected_word.upper())

guess_word()