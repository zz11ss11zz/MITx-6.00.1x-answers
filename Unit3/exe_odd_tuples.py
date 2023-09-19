def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    a = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            a += (aTup[i],)
    return a
        
