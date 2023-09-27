def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    a = []
    for i in aDict.values():
        a.append(len(i))
    b = a.index(max(a))
    return list(aDict.keys())[b]