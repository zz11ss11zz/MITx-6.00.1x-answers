def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    b  = []
    for i in aDict.keys():
        b += aDict[i]
    return len(b)