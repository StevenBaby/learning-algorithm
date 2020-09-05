# coding=utf-8
import itertools
import sys
import re
import copy
import random

import colorama

from fastdict import attrdict

DOT = 1
BOX_GREEN = 2
BOX_RED = 3
BOX_BLUE = 4
DIA_RED = 5
DIA_BLUE = 6


class Engine(object):

    chars = {
        '0': colorama.Fore.WHITE + '□',
        '1': colorama.Fore.WHITE + '●',
        '2': colorama.Fore.GREEN + '■',
        '3': colorama.Fore.RED + '■',
        '4': colorama.Fore.BLUE + '■',
        '5': colorama.Fore.GREEN + '♦',
        '6': colorama.Fore.RED + '♦',
    }

    def __init__(self, queue: list = None, rules=None):
        if queue is None:
            queue = []
        self.rules = rules or {}
        self.raw = queue
        self.queue = copy.deepcopy(queue)
        self.patterns = self.init_patterns()
        self.items = []

    @classmethod
    def put(cls, char):
        if str(char) not in cls.chars:
            return
        colorama.init()
        sys.stdout.write(cls.chars[str(char)])
        colorama.deinit()

    def print_queue(self, queue=None):
        colorama.init()
        if not queue:
            queue = self.queue
        for sequence in queue:
            for char in sequence:
                if char not in self.chars:
                    sys.stdout.write(self.chars['0'])
                    continue
                sys.stdout.write(self.chars[str(char)])
            sys.stdout.write("\n")
        colorama.deinit()

    def print_item(self, idx, index, item):
        sys.stdout.write(f'{colorama.Fore.MAGENTA}{idx:03} {colorama.Fore.CYAN}{index:03} ')
        for char in item:
            self.put(char)
        sys.stdout.write("\n")

    def print_items(self):
        for idx, index, item in self.items:
            self.print_item(idx, index, item)

    def init_patterns(self):
        rules = {}
        for level in self.rules.keys():
            patterns = self.rules[level]
            rules[level] = []
            for var in patterns:
                pat = re.compile(var)
                rules[level].append(pat)
        return rules

    def search_sequence(self, level, pattern, idx, sequence):
        index = 0
        length = len(sequence)
        while index + level <= length:
            string = sequence[index: index + level]
            match = pattern.match(string)
            if not match:
                index += 1
                continue
            item = match.group(0)

            self.print_item(idx, index, item)
            self.items.append((idx, index, item))
            sequence = sequence[:index] + "0" * level + sequence[index + level:]
            index += level
        return sequence

    def search_queue(self, level, pattern):
        backup = []
        for idx, sequence in enumerate(self.queue):
            length = len(sequence)
            if length < level:
                return
            sequence = self.search_sequence(level, pattern, idx, sequence)
            backup.append(sequence)
        self.queue = backup

    def search(self):
        self.items.clear()
        for level, patterns in self.patterns.items():
            for pattern in patterns:
                self.search_queue(level, pattern)


P_BOX_GRE1 = r"(?=(?:[3456]*2[3456]*){1})"
P_BOX_GRE2 = r"(?=(?:[3456]*2[3456]*){2})"
P_BOX_GRE3 = r"(?=(?:[3456]*2[3456]*){3})"
P_BOX_GRE4 = r"(?=(?:[3456]*2[3456]*){4})"
P_BOX_GRE5 = r"(?=(?:[3456]*2[3456]*){5})"
P_BOX_GRE6 = r"(?=(?:2){6})"

P_BOX_RED3 = r"(?=(?:[2456]*3[2456]*){3})"
P_BOX_RED2 = r"(?=(?:[2456]*3[2456]*){2})"
P_BOX_RED1 = r"(?=(?:[2456]*3[2456]*){1})"

P_BOX_BLU2 = r"(?=(?:[2356]*4[2356]*){2})"
P_BOX_BLU1 = r"(?=(?:[2356]*4[2356]*){1})"

P_DIA_GRE2 = r"(?=(?:[234]55[234]+))"
P_DIA_GRE1 = r"(?=(?:[234]5[234]+)|(?:[234]{1,2}5[234]+)|(?:[234]65[234]+))"

P_DIA_RED2 = r"(?=(?:[234]66[234]+))"
P_DIA_RED1 = r"(?=(?:[234]6[2345]+)|(?:[234]{1,2}6[234]+)|(?:[234]56[234]+))"

P_MATCH6 = r'[23456]{6}'
P_MATCH5 = r'[23456]{5}'
P_MATCH4 = r'[23456]{4}'
P_MATCH3 = r'[23456]{3}'
P_MATCH2 = r'[23456]{2}'
P_MATCH1 = r'[23456]{1}'


patterns = {
    (P_BOX_RED3): 3,
    (P_BOX_RED2 + P_BOX_BLU1): 3,
    (P_BOX_RED2 + P_DIA_RED1): 3,
    (P_BOX_RED2 + P_DIA_RED1 + P_BOX_BLU1): 4,
    (P_BOX_RED1 + P_DIA_RED2): 3,
    (P_BOX_RED1 + P_DIA_RED2 + P_BOX_BLU1): 4,
    (P_BOX_BLU2): 2,
    (P_BOX_BLU1): 1,
}

selections = {
    6: [P_BOX_GRE6],
    5: [P_BOX_GRE5],
    4: [P_BOX_GRE4],
    3: [P_BOX_GRE3],
    2: [P_DIA_GRE2, P_BOX_GRE2],
    1: [P_DIA_GRE1, P_BOX_GRE1],
}


def get_rules(remain, pattern):
    if remain <= 0:
        return []
    rules = [
        (remain, pattern + var)
        for var in selections[remain]
    ]
    for var, rule in rules:
        rules = get_rules(remain - 1, rule)
        pass


for level in range(6, 1, -1):
    for pattern, var in patterns.items():
        remain = level - var
        rules = get_rules(remain, pattern)
        print(rules)
exit(0)

# queue = [
#     "43233222233223445656",
#     "3553322333552332534542533324325332",
#     "44443342225566666623",
#     "2222222",
# ]

queue = [
    "11221111222111111111111",
    "111111111112222642121111211111",
    "1163332211111111111111122411",
    "22311222232232322222222222222",
    "11611111222262121112222",
    "22352111111223336222",
]

engine = Engine(queue, rules)

engine.print_queue(queue)
engine.search()
engine.print_queue(engine.queue)


# level = 6
# idx = 0
# sequence = '222222222'

# pattern = P_BOX_GREEN6 + P_MATCH6
# pattern = re.compile(pattern)
# sequence = engine.search_sequence(level, pattern, idx, sequence)

# print(sequence)
