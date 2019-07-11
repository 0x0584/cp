#              File:    chocolates.py
#            Author:    Anas
#
#    Created: <2019-07-10 Wed 17:21:32>
#    Updated: 2019/07/11 19:31:56 by archid-          ###   ########.fr        #
#
# Thoughts: sort the list, from big to small. each time take one of
# `fresh' (non prviously picked) element, max, min, max, ... see if
# it fits a half of the two. if so place it, repeat using the other
#
# J. #247588

def split_into_half(lst, size, halfs = [[], []]):

    return halfs

def choco_test(lst, halfs):
    s = "No"
    if len(halfs) == 2 and sum(lst) == sum(halfs[0]) + sum(halfs[1]):
        s = "Yes"
    print s

###
n_tests = int(input())
tests = []

for i in range(n_tests):
    weights = []
    in_lst = map(int, raw_input().split())
    weights = map(int, raw_input().split())
    assert len(in_lst) == 2 and len(weights) == in_lst[0]
    tests.append([weights] + [in_lst])

for t in tests:
    choco_test(t[0], split_into_half(t[0], t[1][1]))
