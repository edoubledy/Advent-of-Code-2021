def answer_one():
    with open("./src/day2/data/input") as f:
        lines = [line.strip().split(' ') for line in f]

    horizontal_position = 0
    depth = 0

    for line in lines:
        match line:
            case ['forward', x]:
                horizontal_position += int(x)
            case ['down', x]:
                depth += int(x)
            case ['up', x]:
                depth -= int(x)
    
    print(f"Answer One: {horizontal_position * depth}")

if __name__ == '__main__':
    answer_one()
