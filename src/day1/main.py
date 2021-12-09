def part_one():
  with open("./src/day1/data/input") as f:
    lines = [int(line.strip()) for line in f]
  
  ans = 0
  for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
      ans += 1

  return ans

def part_two():
  with open("./src/day1/data/input") as f:
    lines = [int(line.strip()) for line in f]

  ans = 0
  for i in range(0, len(lines)):
    window = sum(lines[i:i+2])
    prev_window = sum(lines[i-1:i+1])

    if window > prev_window:
      ans += 1

  return ans

if __name__ == '__main__':
  print("Answer One: " + str(part_one()))
  print("Answer Two: " + str(part_two()))
