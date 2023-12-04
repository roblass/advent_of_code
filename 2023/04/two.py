#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def compute_matches(card_line):
    card_number = card_line.split()[1][:-1]

    pos = card_line.find("|")
    winners = set(card_line[:pos].split()[2:])

    my_numbers = card_line[pos:].split()[1:]

    num_winners = 0
    for number in my_numbers:
        if number in winners:
            num_winners += 1

    return card_number, num_winners

def main(filename):
    card_matches = {}
    with open(filename, "r") as cardfile:
        num_cards = 0
        for line in cardfile:
            card_number, matches = compute_matches(line)
            card_matches[int(card_number)] = matches
            num_cards += 1
    print(card_matches)

    cards_owned = {c: 1 for c in card_matches}
    for card in range(1, num_cards + 1): # process each card
        for _ in range(cards_owned[card]): # do it once per card of this type
            if card_matches[card] > 0:
                for i in range(card+1, card + card_matches[card] + 1):
                    cards_owned[i] += 1

    print(cards_owned)
    print(sum(cards_owned.values()))


if __name__ == '__main__':
    main(sys.argv[1])
