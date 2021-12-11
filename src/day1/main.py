import time

def time_func(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(func.__name__ + " time (s): " + str(round(end - start, 6)))
    
    return wrapper

@time_func
def answer_one():
    with open("./src/day1/data/input") as f:
        lines = [int(line.strip()) for line in f]

    ans = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i-1]:
            ans += 1

    print(f"Answer One: {ans}")

if __name__ == '__main__':
    answer_one()
