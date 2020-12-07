#posh teal bags contain 2 faded coral bags, 3 striped crimson bags, 1 faded red bag.
import sys
from collections import defaultdict

goesin = defaultdict(list)
for rule in open(sys.argv[1], 'r'):
    section = rule[:-1].split(',')
    #first one
    outer = ' '.join(section[0].split()[0:2])
    goesin[' '.join(section[0].split()[5:7])].append(outer)
    for s in section[1:]:
        goesin[' '.join(s.split()[1:3])].append(outer)

def find_pots(target="shiny gold", pots=[]):
    new_pots = [p for p in goesin[target] if p not in pots]
    if len(set(new_pots) - set(pots)) == 0:
        return []
    else:
        pots.extend(new_pots)
        for pot in new_pots:
            pots.extend(find_pots(pot, pots))
        return list(set(pots))

print(len(set(find_pots())))
