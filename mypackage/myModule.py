def top_n(items, n):
    """
    Return the top n items in a array, in dsc order.
    args:
        Items (array): list or array-like objects
        n (init): number of items to return
    Return:
        array: top n items , in dsc order
    
    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,3]
    """
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]: # if this item is bigger than the next item...
                items[j], items[j+1] = items[j+1] ,items[j] #swap the two
    #get last two items
    top_n = top_n[-n:]

    #return in descnding order
    return top_n[::-1]

