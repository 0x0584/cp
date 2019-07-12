#              File:    manal_permus.py
#            Author:    Anas
#
#    Created: <2019-07-12 Fri 11:54:12>
#    Updated: <2019-07-12 Fri 13:42:22>
#
# Thoughts: each time, pick an element, remove it from a tmp list,
# and recursively pick another from that same tmp list until there
# are no more elements
#
# I. #247588

def permut_list(lst):
    permus = []
    unique = []

    if not lst:
            return [[]]
    for e in lst:
        temp = lst[:]
        temp.remove(e)
        print temp
        permus.extend([[e] + r for r in permut_list(temp)])
    for e in permus:
        if e not in unique:
            unique.append(e)
    return unique

print permut_list([1, 2, 3])

# n_tests = input()
# tests = []
# for i in range(n_tests):
#     tests.append([input(), map(int, raw_input().split())])

# for t in tests:
#     print int(len(permut_list(t[1])) % (1e9 + 7))
