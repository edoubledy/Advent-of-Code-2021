import time

def time_func(func):
    def wrapper(func):
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    
    return wrapper