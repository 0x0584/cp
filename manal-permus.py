#              File:    manal_permus.py
#            Author:    Anas
#
#    Created: <2019-07-12 Fri 11:54:12>
#    Updated: <2019-07-12 Fri 17:36:07>
#
# Thoughts: this is an iterative approach, specifiing a direction to
# move the iterable items. left and right; -1 and 1, respectively.
# find the biggest element, keep it's index. reverse the direction of
# all bigger numbers. then swap the element with the one next to it's
# direction. repeat until we reach the length of `orilst'.
#
# I. #247588

class Elem:
    def __init__(self, element, direction):
        self.element = element
        self.direction = direction

def permut_list(lst):
    orilst = sorted([Elem(element, -1) for element in lst],
                         key = lambda e: e.element)
    perms = []

    while True:
        foo = [e.element for e in orilst]
        if foo not in perms:
            perms.append(foo)
        to_move = None
        for i, e in enumerate(orilst):
            j = i + e.direction
            if (0 <= j < len(orilst) and
                e.element > orilst[j].element and
                (to_move is None or e.element > tmp)):
                to_move = i
                tmp = orilst[to_move].element
        if to_move is None:
            break
        for e in orilst:
            if e.element > orilst[to_move].element:
                e.direction *= -1
        i = to_move
        j = i + orilst[i].direction
        orilst[i], orilst[j] = orilst[j], orilst[i]
    return perms

# print int(len(permut_list([1, 2, 3, 4, 5])) % (1e9 + 7))

n_tests = input()
tests = []
for i in range(n_tests):
    tests.append([input(), map(int, raw_input().split())])

for t in tests:
    print t
    print int(len(permut_list(t[1])) % (1e9 + 7))
