DEBUG = False

with open('5.txt', 'r') as file:
    code = list(map(int, (file.read().split(','))))


#code = list(map(int, '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'.split(',')))


def get_codes(instruction):
    inst = str(instruction)[::-1]
    opcode = int(inst[0:2][::-1])
    if DEBUG:
        print("Instruction: " + str(instruction))
    try:
        mode1 = int(inst[2])
    except IndexError:
        mode1 = 0
    try:
        mode2 = int(inst[3])
    except IndexError:
        mode2 = 0
    try:
        mode3 = int(inst[4])
    except IndexError:
        mode3 = 0
    return opcode, mode1, mode2, mode3


def computer(input):
    i = 0
    while True:
        opcode, mode1, mode2, mode3 = get_codes(code[i])
        if DEBUG:
            print(code)
            print("Opcode: " + str(opcode) + ", mode1: " + str(mode1) + ", mode2: " + str(mode2) + ", mode3: " + str(mode3))
        if opcode == 99:
            if DEBUG:
                print("Finished!")
            break
        elif opcode == 1:
            if DEBUG:
                print("Var1: " + str(code[i+1]) + ", var2: " + str(code[i+2]) + ", var3: " + str(code[i+3]))
            output = code[i + 3]
            if mode1 == 0:
                add1 = code[code[i+1]]
            elif mode1 == 1:
                add1 = code[i+1]
            if mode2 == 0:
                add2 = code[code[i+2]]
            elif mode2 == 1:
                add2 = code[i+2]
            value = add1 + add2
            code[output] = value
            i += 4
        elif opcode == 2:
            if DEBUG:
                print("Var1: " + str(code[i + 1]) + ", var2: " + str(code[i + 2]) + ", var3: " + str(code[i + 3]))
            output = code[i + 3]
            if mode1 == 0:
                add1 = code[code[i+1]]
            elif mode1 == 1:
                add1 = code[i+1]
            if mode2 == 0:
                add2 = code[code[i+2]]
            elif mode2 == 1:
                add2 = code[i+2]
            value = add1 * add2
            code[output] = value
            i += 4
        elif opcode == 3:
            if DEBUG:
                print("Var1: " + str(code[i + 1]))
            if mode1 == 0:
                code[code[i+1]] = input
            elif mode1 == 1:
                code[i+1] = input
            i += 2
        elif opcode == 4:
            if DEBUG:
                print("Var1: " + str(code[i + 1]))
            if mode1 == 0:
                input = code[code[i+1]]
            elif mode1 == 1:
                input = code[i+1]
            i += 2
        elif opcode == 5:
            if DEBUG:
                print("Var1: " + str(code[i + 1]) + ", var2: " + str(code[i + 2]))
            if mode1 == 0:
                value = code[code[i + 1]]
            elif mode1 == 1:
                value = code[i+1]
            if value != 0:
                if mode2 == 0:
                    i = code[code[i + 2]]
                elif mode2 == 1:
                    i = code[i + 2]
            else:
                i += 3
            if DEBUG:
                print("Index: " + str(i))
        elif opcode == 6:
            if DEBUG:
                print("Var1: " + str(code[i+1]) + ", var2: " + str(code[i+2]))
            if mode1 == 0:
                value = code[code[i + 1]]
            elif mode1 == 1:
                value = code[i+1]
            if value == 0:
                if mode2 == 0:
                    i = code[code[i + 2]]
                elif mode2 == 1:
                    i = code[i + 2]
            else:
                i += 3
            if DEBUG:
                print("Index: " + str(i))
        elif opcode == 7:
            if DEBUG:
                print("Var1: " + str(code[i + 1]) + ", var2: " + str(code[i + 2]) + ", var3: " + str(code[i + 3]))
            if mode1 == 0:
                first = code[code[i + 1]]
            elif mode1 == 1:
                first = code[i + 1]
            if mode2 == 0:
                second = code[code[i + 2]]
            elif mode2 == 1:
                second = code[i + 2]
            if first < second:
                code[code[i + 3]] = 1
            else:
                code[code[i + 3]] = 0
            i += 4
        elif opcode == 8:
            if DEBUG:
                print("Var1: " + str(code[i + 1]) + ", var2: " + str(code[i + 2]) + ", var3: " + str(code[i + 3]))
            if mode1 == 0:
                first = code[code[i + 1]]
            elif mode1 == 1:
                first = code[i + 1]
            if mode2 == 0:
                second = code[code[i + 2]]
            elif mode2 == 1:
                second = code[i + 2]
            if first == second:
                code[code[i + 3]] = 1
            else:
                code[code[i + 3]] = 0
            i += 4
    return input


print("Final output: " + str(computer(5)))










