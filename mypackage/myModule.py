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
        [8,7,4]
    """
    for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items) - 1 - i):
            if items[j] > items[j+1]:  # If this item is bigger than the next item...
                items[j], items[j+1] = items[j+1], items[j]  # Swap the two
    
    # Get the last n items
    top_n = items[-n:]

    # Return in descending order
    return top_n[::-1]

