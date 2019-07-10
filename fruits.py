#              File:    fruits.py
#            Author:    Anas
#
#    Created: <2019-07-10 Wed 09:49:31>
#    Updated: <2019-07-10 Wed 16:32:22>
#
# Thoughts: the idea is to find a variable `a' such that `k = a [n]'
#
# E. #247588

n_tests = int(input())
assert 1 <= n_tests <= 1e5

tests = []
for t in range(n_tests):
    tests.append(map(int, raw_input().split()))
for r in tests:
    print r[1] % r[0]
