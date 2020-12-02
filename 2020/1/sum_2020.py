for n in open('input.txt', 'r').read().split('\n'):
    for m in open('input.txt', 'r').read().split('\n'):
        for o in open('input.txt', 'r').read().split('\n'):
            try:
                if int(n) + int(m) + int(o) == 2020:
                    print(f'{n} * {m} * {o}')
            except:
                pass
