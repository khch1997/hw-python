import time

def calculate_time(func):
    """
    Calculate and print the time to run a function in seconds.

    Parameters
    ----------
    func : function
        The function to run

    Examples
    --------
    def func():
        time.sleep(2)
        
    >>> calculate_time(func)
    2.0001738937
    """
    current = time.time()
    func()
    end = time.time()
    print(f'Total time {end - current}')