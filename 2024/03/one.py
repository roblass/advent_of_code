# -*- coding: utf-8 -*-
import sys


class Parser:
    def __init__(self):
        self.so_far = ""
        self.in_mul = False
        self.in_op1 = False
        self.in_op2 = False

    def reset(self):
        self.so_far = ""
        self.in_mul = False
        self.in_op1 = False
        self.in_op2 = False

    def is_expected(self, t):
        if self.in_mul:
            self.so_far += t
            #print(f"\t so_far = {self.so_far}")
            if self.so_far in ("mu", "mul"):
                return True
            if self.so_far in ("mul("):
                self.in_mul = False
                self.in_op1 = True
                return True
            self.reset()
            return False
        if self.in_op1:
            if t.isdigit():
                self.so_far += t
                return True
            if t == ",":
                self.so_far += t
                self.in_op1 = False
                self.in_op2 = True
                return True
            self.reset()
            return False
        if self.in_op2:
            if t.isdigit():
                self.so_far += t
                return True
            if t == ")":
                self.so_far += t
                return True
            self.reset()
            return False
        if t == "m":
            self.so_far = t
            self.in_mul = True
            return True
        return False

    def evaluate(self):
        nums = self.so_far[4:-1].split(",")
        return int(nums[0]) * int(nums[1])

    def add_token(self, t):
        is_expected = self.is_expected(t)
        #print(f"Got token {t} and is_expected = {is_expected}")
        if is_expected and self.so_far.endswith(")"):
            print(f"need to evaluate {self.so_far}")
            result = self.evaluate()
            self.reset()
            return result
        if not is_expected:
            self.reset()
        return 0


with open(sys.argv[1], "r", encoding="utf-8") as file:
    p = Parser()
    total = 0
    for line in file:
        for c in line:
            total += p.add_token(c)

print(total)
