#              File:    big-pow.c
#            Author:    Anas
#       Description:    the idea is to keep only the last k-digits using
#                       modular arithmetic
#
#         Created: <2019-07-08 Mon 17:01:21>
#         Updated: <2019-07-10 Wed 08:35:37>
#
# D. #247588

import sys

def last_digit(a, n, k):
    assert 1 <= a <= 1e5 and 1 <= n <= 1e5 and 1 <= k <= 9
    result = 1
    for i in range(n):
        result =  (a * result) % 10**k
    return result

n_tests = int(input())
arr = []
for i in range(n_tests):
    arr.append(map(int, raw_input().split()))

for i in range(n_tests):
    s = 0
    for c in str(last_digit(arr[i][0], arr[i][1], arr[i][2])): # a, n, k
        s = s + int(c);
    print s

#                               -*- 0x0584 -*-
