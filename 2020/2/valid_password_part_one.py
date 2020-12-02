from collections import Counter

invalid = valid = 0

for number, letter, password in [l.split(' ') for l in open('input.txt', 'r').read().split('\n')[:-1]]:
    min, max = [int(n) for n in number.split('-')]
    c = Counter(password)
    if c[letter[0]] < min or c[letter[0]] > max:
        invalid += 1
    else:
        valid += 1

print(f'valid = {valid}; invalid = {invalid}')
