def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
      
     * remind to use previous defined function: 
       getGuessedWord & getGuessedWord

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long." %len(secretWord))
    print("-----------")
    i = 8
    b = [] # for comparison
    c = [] # for print

    while i > 0:
        print("You have %d guesses left" %i)
        print("Available letters:", getAvailableLetters(c))
        a = input("please guess a letter: ").lower()
        if a in b:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, b))
            print("------------")
        elif a in secretWord:
            b.append(a)
            c.append(a)
            print("Good guess:", getGuessedWord(secretWord, b))
            print("------------")
            if set(b) == set(secretWord):
                print("Congratulations, you won!")
                break
        else:
            c.append(a)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, b))
            print("------------")
            i -= 1
            if i == 0:
                print("Sorry, you ran out of guesses. The word was", secretWord)
                break