if __name__ == "__main__":
    inputs = []
    with open('data/input_day1.txt') as f:
        inputs = [l.rstrip('\n') for l in f]

    for i in range(len(inputs)):
        for j in range(len(inputs)):
            for k in range(len(inputs)):
                if int(inputs[i])+int(inputs[j])+int(inputs[k]) == 2020:
                    print(int(inputs[i])*int(inputs[j])*int(inputs[k]))

