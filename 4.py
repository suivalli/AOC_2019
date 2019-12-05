range_lower = 171309
range_upper = 643603


def get_passwords_1(lower, upper):
    passwords = []
    for i in range(lower, upper+1):
        x = list(map(int, str(i)))
        if x == sorted(x):
            if len(x) != len(set(x)):
                passwords.append(x)
    return passwords


def get_passwords_2(lower, upper):
    passwords = []
    for i in range(lower, upper+1):
        x = list(map(int, str(i)))
        if x == sorted(x):
            nums = []
            for j in range(0, len(x)-1):
                if x[j] == x[j+1]:
                    nums.append([x[j], x[j+1]])
            unique = False
            for k in nums:
                if nums.count(k) == 1:
                    unique = True
            if unique is True:
                passwords.append(x)

    return passwords


passwords = get_passwords_2(range_lower, range_upper)

print(passwords)
print(len(passwords))
