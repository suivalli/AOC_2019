

def get_input(noun,verb):
    with open('2.csv', 'r') as file:
        input = list(map(int, (file.read().split(','))))
    input[1] = noun
    input[2] = verb
    return input

output = 0


def get_output():
    while True:
        for x in range(0, 101):
            for k in range(0, 101):
                input = get_input(x, k)
                for i in range(0, len(input), 4):
                    if input[i] == 99:
                        break
                    elif input[i] == 1:
                        input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
                    elif input[i] == 2:
                        input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
                output = input[0]
                if output == 19690720:
                    return input

output = get_output()

print(100 * output[1] + output[2])









