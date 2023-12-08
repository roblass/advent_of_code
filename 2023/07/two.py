#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from enum import Enum
from collections import Counter, defaultdict

#247091178 is too low

class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        # figure out what kind of hand this is

        self.hand_type = self.get_modified_hand_type(hand)

        self.scores = {
            "J": -1,
            "2": 0,
            "3": 1,
            "4": 2,
            "5": 3,
            "6": 4,
            "7": 5,
            "8": 6,
            "9": 7,
            "T": 8,
            "Q": 10,
            "K": 11,
            "A": 12,
        }


    def get_hand_type(self, hand):
        c = Counter(hand)
        if len(c) == 1:
            hand_type = HandType.FIVE_OF_A_KIND
        elif len(c) == 2 and set(c.values()) == {1, 4}:
            hand_type = HandType.FOUR_OF_A_KIND
        elif len(c) == 2 and set(c.values()) == {2, 3}:
            hand_type = HandType.FULL_HOUSE
        elif len(c) == 3 and set(c.values()) == {1, 3}:
            hand_type = HandType.THREE_OF_A_KIND
        elif len(c) == 3 and set(c.values()) == {1, 2}:
            hand_type = HandType.TWO_PAIR
        elif len(c) == 4 and set(c.values()) == {1, 2}:
            hand_type = HandType.ONE_PAIR
        elif len(c) == 5 and set(c.values()) == {1}:
            hand_type = HandType.HIGH_CARD
        return hand_type


    def get_modified_hand_type(self, hand):
        if "J" not in hand:
            return self.get_hand_type(hand)

        hand_type = self.get_hand_type(hand)
        if hand_type == HandType.FIVE_OF_A_KIND:
            return HandType.FIVE_OF_A_KIND
        if hand_type == HandType.FOUR_OF_A_KIND:
            return HandType.FIVE_OF_A_KIND
        if hand_type == HandType.FULL_HOUSE:
            return HandType.FIVE_OF_A_KIND
        if hand_type == HandType.THREE_OF_A_KIND:
            return HandType.FOUR_OF_A_KIND
        if hand_type == HandType.TWO_PAIR:
            if hand.count("J") == 2:
                return HandType.FOUR_OF_A_KIND
            return HandType.FULL_HOUSE
        if hand_type == HandType.ONE_PAIR:
            return HandType.THREE_OF_A_KIND
        if hand_type == HandType.HIGH_CARD:
            return HandType.ONE_PAIR


    def __eq__(self, other):
        if set(self.hand) == set(other.hand):
            return True
        return False


    def __str__(self):
        return f"{self.hand}: {self.hand_type}"


    def __repr__(self):
        return f"{self.hand}: {self.hand_type}"


    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            i = 0
            while i < 5 and self.scores[self.hand[i]] == self.scores[other.hand[i]]:
                i += 1
            if i == 5:
                print("what the fuck, AoC")
                return False
            return self.scores[self.hand[i]] < self.scores[other.hand[i]]
        return self.hand_type < other.hand_type


    def __gt__(self, other):
        if self.hand_type == other.hand_type:
            i = 0
            while i < 5 and self.scores[self.hand[i]] == self.scores[other.hand[i]]:
                i += 1
            if i == 5:
                print("what the fuck, AoC")
                return False
            return self.scores[self.hand[i]] > self.scores[other.hand[i]]
        return self.hand_type > other.hand_type


def main(filename):
    with open(filename, "r") as data:
        hands_by_type = defaultdict(list)
        for line in data:
            hand, bid = line.split()
            hand = Hand(hand, int(bid))
            hands_by_type[hand.hand_type].append(hand)
    print(hands_by_type)

    ranked_hands = []
    for hand_type in [HandType.HIGH_CARD, HandType.ONE_PAIR, HandType.TWO_PAIR,
                      HandType.THREE_OF_A_KIND, HandType.FULL_HOUSE, HandType.FOUR_OF_A_KIND,
                      HandType.FIVE_OF_A_KIND]:
        hands_by_type[hand_type].sort()
        ranked_hands.extend(hands_by_type[hand_type])

    print(list(enumerate(ranked_hands)))
    total_winnings = 0
    for rank, hand in enumerate(ranked_hands):
        total_winnings += (rank+1) * hand.bid

    print(total_winnings)

if __name__ == '__main__':
    main(sys.argv[1])
