from collections import defaultdict

last_digit = defaultdict(list)
for n in open('input.txt', 'r').read().split('\n')[:-1]:
    n = int(n)
    last_digit[n % 10].append(n)

# handle zero and five
for index in [0, 5]:
    for n1 in last_digit[index]:
        for n2 in last_digit[index]:
            if n1 + n2 == 2020:
                print(f'{n1} * {n2} = {n1 * n2}')


# handle all the other final digits
for i in range(1, 5):
    for n1 in last_digit[0 + i]:
        for n2 in last_digit[10 - i]:
            if n1 + n2 == 2020:
                print(f'{n1} * {n2} = {n1 * n2}')
