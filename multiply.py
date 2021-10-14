def multiply_list(nums):
    """
    Multiply elements in a list.

    Parameters
    ----------
    nums : list of int
        elements as input in a list.

    Returns
    -------
    int:
        The product of all elements.
    
    False:
        If any element in the list is invalid.

    Examples
    --------
    >>> multiply_list([])
    False
    >>> multiply_list([1, 2, 3, 4, 5])
    120
    >>> multiply_list([1, 2, 'a', 4, 5])
    False
    """
    product = 1
    for num in nums:
        if type(num) != int:
            return False
        product *= num
    return product