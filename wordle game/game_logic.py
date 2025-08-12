# task 6.1: backend
import random
score = 0
def guess_word():

    def load_words(words):
        with open(words, "r") as f:
            words = [word.strip().lower() for word in f if len(word.strip()) == 5]
        
        return words, set(words)
    words, word_set = load_words("words.txt")
    if user_guess.lower() in word_set:
        print ("Your guess is accepted")
    else:
        print("Incorect guess")
        score -=1

    selected_word = random.choice (words)
    
    user_guess = input("guess the word: ")
    if len(user_guess) != 5:
        user_guess = input ("The word must be 5 letters, please try again: ")
    for n in range(5):
        if user_guess == selected_word:
            print ("Congrats! you've guessed the right word in " + str(n+1) + " attempts")
            break
        else:
            print ("That's not correct please try again")
            user_guess = input("guess the word: ")
            continue
    else:
        print("you're out of attempts! The word was " + selected_word)
        
    # task 6.2 and task 6.3:
    grid = [["" for_in range(5)] for_in range(6)]
   
    guess_list = list(user_guess)
    selected_list = list(selected_word)
    
    for i in range (4):
        if guess_list[i] == selected_list[i]:
            print ("\033[92m" + guess_list[i] + "\033[0m")
        elif guess_list[i] in selected_list:
            print ("\033[93m" + guess_list[i] + "\033[0m")
        else:
            print("\033[90m" + guess_list[i] + "\033[0m")

