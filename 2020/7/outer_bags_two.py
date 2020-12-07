#posh teal bags contain 2 faded coral bags, 3 striped crimson bags, 1 faded red bag.
import sys
from collections import defaultdict

comesfrom = defaultdict(list)
terminals = []
for rule in open(sys.argv[1], 'r'):
    if "contain no other bags" in rule:
        terminals.append(' '.join(rule.split()[0:2]))
        continue
    section = rule[:-1].split(',')
    #first one
    outer = ' '.join(section[0].split()[0:2])
    comesfrom[outer].append((int(section[0].split()[4]), ' '.join(section[0].split()[5:7])))
    for s in section[1:]:
        comesfrom[outer].append((int(s.split()[0]), ' '.join(s.split()[1:3])))

def find_pots(target="shiny gold"):
    new_pots = comesfrom[target]
    bags_needed = 0
    for number, pot in new_pots:
        if pot in terminals:
            bags_needed += number
        else:
            # the nested bags in EACH outer bag, plus the correct number of outer bags
            bags_needed += (number * find_pots(pot)) + number
    return bags_needed

print(find_pots())
