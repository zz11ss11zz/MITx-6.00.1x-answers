def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    a = hand.copy()
    m = 0
    if word in wordList:
        for i in word:
            if i in hand:
                m += 1
                a[i] = a[i] - 1
                if a[i] < 0:
                    return False
        if m == len(word):
            return True
        else:
            return False
    else:
        return False