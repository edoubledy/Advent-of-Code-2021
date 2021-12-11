def answer_one():
    with open("./src/day1/data/input") as f:
        lines = [int(line.strip()) for line in f]

    ans = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i-1]:
            ans += 1

    print(f"Answer One: {ans}")

def answer_two():
    with open("./src/day1/data/input") as f:
        lines = [int(line.strip()) for line in f]

    ans = 0
    for i in range(1, len(lines) - 2):
        if lines[i+2] > lines[i-1]:
            ans += 1

    print(f"Answer Two: {ans}")

if __name__ == '__main__':
    answer_one()
    answer_two()