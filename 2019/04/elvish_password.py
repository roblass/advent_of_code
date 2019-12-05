import sys

potential_passwords = []
for num in range(sys.argv[1], sys.argv[2]):
    good = False
    s_num = str(num)
    for i in range(5):
        if s_num[i] == s_num[i + 1]:
            good = True
        if s_num[i] > s_num[i + 1]:
            good = False
            break
    if not good:
        continue
    potential_passwords.append(num)

print(len(potential_passwords))
print(potential_passwords)
