# task 6.1: backend
def guess_word ():
    import random
    words_5 = ["beach", "ocean", "river", "paint", 
               "happy", "drums", "radio", "tiger", 
               "bread", "pixel", "paint", "drill", 
               "truck", "shirt", "virus", "comet"]
    selected_word = random.choice(words_5)
    
    for n in range(6):
        user_guess = input("guess the word: ")
        if selected_word == user_guess:
            print ("Congrats! you've guessed the right word in " + str(n) + " attempts")
            break
        else:
            print ("That's not correct please try again")
            print ("You have " + str(5 - n) + " attempts left")

guess_word ()
