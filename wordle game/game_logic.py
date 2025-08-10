# task 6.1: backend
def guess_word ():
    import random
    words_5 = {"beach", "ocean", "river", "paint", 
               "happy", "drums", "radio", "tiger", 
               "bread", "pixel", "paint", "drill", 
               "truck", "shirt", "virus", "comet"}
    selected_word = random.choice (words_5)
    
    user_guess = input("guess the word: ")
    for n in range(6):
        if selected_word == selected_word:
            print ("Congrats! you've guessed the right word in " + n + " attempts")
        else:
            print ("That's not correct please try again")

guess_word ()



