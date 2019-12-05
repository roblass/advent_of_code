import sys

potential_passwords = []
for num in range(sys.argv[1], sys.argv[2]):
    good = False
    s_num = str(num)
    for i in range(5):
        if s_num[i] == s_num[i + 1]:
            # exclude 3 or more in a row not at beginning
            if i in [1, 2, 3, 4] and s_num[i - 1] == s_num[i + 1]:
                pass
            # exclude 3 or more in a row at the beginning
            elif i in [0, 1, 2, 3] and s_num[i] == s_num[i + 2]:
                pass
            else:
                good = True
        if s_num[i] > s_num[i + 1]:
            good = False
            break
    if not good:
        continue

    potential_passwords.append(num)

print(len(potential_passwords))
