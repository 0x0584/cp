#              File:    manal_permus.py
#            Author:    Anas
#
#    Created: <2019-07-12 Fri 11:54:12>
#    Updated: <2019-07-12 Fri 14:40:17>
#
# Thoughts: each time, pick an element, remove it from a tmp list,
# and recursively pick another from that same tmp list until there
# are no more elements
#
# I. #247588
from itertools import count

# Directions in which an element may be moving.
_LEFT = -1
_RIGHT = 1

class PermutationElement:
    "Element of a permutation, with its current direction."
    def __init__(self, element, direction):
        assert direction in (_LEFT, _RIGHT)
        self.element = element
        self.direction = direction

# Mapping from direction to corresponding format string.
_FORMAT = {_LEFT: " <{}", _RIGHT: " {}>"}

def print_permutations(iterable):
    "Print the permutations of an iterable in plain changes order."
    # Build initial state, with all elements moving left.
    permutation = [PermutationElement(element, _LEFT) for element in iterable]

    for n in count(1):
        # Print the permutation.
        print "{}.".format(n)
        for e in permutation:
            print _FORMAT[e.direction].format(e.element)
        print("")

        # Find the index of the largest mobile element in the permutation.
        mobile = None
        for i, e in enumerate(permutation):
            j = i + e.direction
            if (0 <= j < len(permutation)
                and e.element > permutation[j].element
                and (mobile is None or e.element > mobile_element)):
                mobile = i
                mobile_element = permutation[mobile].element
        if mobile is None:
            print("#####END#####")
            break

        # Reverse direction of elements larger than the mobile element.
        for e in permutation:
            if e.element > mobile_element:
                e.direction *= -1

        # Update permutation by moving the mobile element in its direction.
        i = mobile
        j = i + permutation[i].direction
        assert 0 <= j < len(permutation)
        permutation[i], permutation[j] = permutation[j], permutation[i]

print print_permutations([1, 2, 3, 4])

# n_tests = input()
# tests = []
# for i in range(n_tests):
#     tests.append([input(), map(int, raw_input().split())])

# for t in tests:
#     print int(len(permut_list(t[1])) % (1e9 + 7))
