def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    # FILL IN YOUR CODE HERE...a = list(secretWord)
    n = 0
    a = list(secretWord)
    for i in a:
        if i in lettersGuessed:
            n += 1
    if n == len(secretWord):
        return True
    else:
        return False