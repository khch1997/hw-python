import time

def calculate_time(func):
    current = time.time()
    func()
    end = time.time()
    print(f'Total time {end - current}')