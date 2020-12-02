invalid = valid = 0

for number, letter, password in [l.split(' ') for l in open('input.txt', 'r').read().split('\n')[:-1]]:
    letter = letter[0]
    min, max = [int(n) -1 for n in number.split('-')]
    if (letter in password[min] and letter not in password[max]) or \
            (letter not in password[min] and letter in password[max]):
        valid += 1
    else:
        invalid += 1

print(f'valid = {valid}; invalid = {invalid}')
