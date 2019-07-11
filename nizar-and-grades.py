#              File:    nizar-and-grades.py
#            Author:    Anas
#
#    Created: <2019-07-10 Wed 09:08:32>
#    Updated: <2019-07-11 Thu 22:01:51>
#
# Thoughts: I was wrong! the idea is to give a count of how many grades
# are between min and max
#
# D. #247588

def find_best(grades):
    unique = list(set(sorted(grades)))
    unique.remove(max(unique))
    if len(unique) == 0:
        return 0
    unique.remove(min(unique))
    return len(unique)

# print find_best([0, 3, 4, 1, 5, 1, 2, 5])
# print find_best([1, 2, 3, 4, 5])

n_tests = int(input())
tests = []
for t in range(n_tests):
    tests.append([int(input()),
                  map(int, raw_input().split())])
for t in tests:
    print find_best(t[1])
