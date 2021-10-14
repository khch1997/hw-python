def tripler(func):
    """
    Call the function func that this function is used on three times.

    Parameters
    ----------
    func : function
        The function to run

    Examples
    --------
    def func():
        print("Hello")

    >>> tripler(func)
    Hello
    Hello
    Hello
    """
    def wrapper():
      func()
      func()
      func()
    return wrapper