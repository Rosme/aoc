import re

def solution_1(inputs):
    r = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

    validCount = 0
    for line in inputs:
        match = r.match(line)

        if match:
            occurences = match.group(4).count(match.group(3))

            if occurences >= int(match.group(1)) and occurences <= int(match.group(2)):
                validCount += 1


    print(validCount)

def solution_2(inputs):
    r = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

    validCount = 0
    for line in inputs:
        match = r.match(line)

        if match:
            firstPos = int(match.group(1))-1
            secondPos = int(match.group(2))-1
            c = match.group(3)[0]
            password = match.group(4)

            if (password[firstPos] == c and password[secondPos] != c) or (password[firstPos] != c and password[secondPos] == c):
                validCount += 1


            


    print(validCount)


if __name__ == "__main__":
    inputs = []

    with open('data/input_day2.txt') as f:
        inputs = [l.rstrip('\n') for l in f]

    solution_1(inputs)
    solution_2(inputs)
