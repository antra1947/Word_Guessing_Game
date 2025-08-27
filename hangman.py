def Hangman():

    import random

    f=open('wordlist.txt','r') #just create a file with the words to be used in the game
    f1=open('record.txt','a')

    words=f.read().splitlines() 
    #using splitlines() instead of f.readlines() to avoid end of line character while viewing the written data 
    
    word = random.choice(words[:-1])
    comma=","

    allowed_errors = 3      
    User=input("Enter Your Name : ")
    guesses = []

    done = False 
 
    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter,end=" ")
            else:
                print("_",end=" ")
        print("")


        guess = input(f"Allowed Errors Left{allowed_errors},Next guess : ")
        guesses.append(guess.lower())

        if guess.lower() not in word.lower():
            allowed_errors -= 1

            if allowed_errors == 0:
                break

        done = True

        for letter in word:
            if letter.lower() not in guesses:
                done = False

    if done:
        print(f"You have found the word ! It was {word}!")
        f1.write(f"{User}{comma}Guessed the word ! It was {word}!\n")
    else:
        print(f"Game Over ! The word was {word} ! \n")
        f1.write(f"{User}{comma}failed to Guess the word! It was {word}! \n")
                 
                 
                
