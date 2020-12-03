for n in open('input.txt', 'r').read().split('\n'):
    for m in open('input.txt', 'r').read().split('\n'):
        try:
            if int(n) + int(m) == 2020:
                print(f'{n} * {m} = {int(n) * int(m)}')
        except:
            pass
