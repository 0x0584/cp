#              File:    nizar-and-grades.py
#            Author:    Anas
#
#    Created: <2019-07-10 Wed 09:08:32>
#    Updated: <2019-07-10 Wed 09:47:26>
#
# Thoughts: sort the grades, remove duplicated, get the middle. it
# might contain more than one if the length of the grades is pair
#
# D. #247588

def find_best(grades):
    grades.sort()
    unique = list(set(grades))
    unique_len = len(unique)
    if unique_len % 2 == 0:
        return [unique[unique_len / 2 - 1],
                unique[unique_len / 2]]
    return [unique[unique_len / 2]]

n_tests = int(input())
tests = []
for t in range(n_tests):
    tests.append([int(input()),
                  map(int, raw_input().split())])
for t in tests:
    print " ".join([str(g) for g in find_best(t[1])])
