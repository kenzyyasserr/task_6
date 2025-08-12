import random
score = 0

def guess_word():
    global score
    
    #loading the dataset
    def load_words(words):
        with open(words, "r") as f:
            words = [word.strip().lower() for word in f if len(word.strip()) == 5]
        return words, set(words)
    
    words, word_set = load_words("words.txt")

 #selecting the word + making the grid
    selected_word = random.choice (words)
    grid = [[" " for _ in range(5)] for _ in range(6)]
    
    for attempt in range(6):
        #input is only 5 letters
        while True:
            user_guess = input("Guess the 5 letter word: ").lower()
            if len(user_guess) != 5:
                print("The word must be 5 letters, please try again!")
            else:
                break

        guess_list = list(user_guess)
        selected_list = list(selected_word)

        if user_guess.lower() in word_set:
            print ("Your guess is accepted")
        else:
            print("Incorect guess")
            score -=5
        
        if user_guess == selected_word:
            print("Congrats! you have guessed the right word from the first try!")
            score +=10

        for col, letter in enumerate(user_guess):
            grid[attempt][col] = letter.lower()
        print(guess_list)
        
        #comparing the letters
        for i in range (5):
            if guess_list[i] == selected_list[i]:
                print ("\033[92m" + guess_list[i] + "\033[0m")
                
            elif guess_list[i] in selected_list:
                print ("\033[93m" + guess_list[i] + "\033[0m")
                
            else:
                print("\033[90m" + guess_list[i] + "\033[0m")

    if user_guess == selected_word:
        print ("Congrats! you've guessed the right word in " + str(n+1) + " attempts")

        #score calculation
        score += max(5 - attempt, 1)  #more points for fewer attempts
    else:
        print("you're out of attempts! The word was " + selected_word)

guess_word()
print ("Your score is " + str(score))