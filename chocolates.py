#              File:    chocolates.py
#            Author:    Anas
#
#    Created: <2019-07-10 Wed 17:21:32>
#    Updated: <2019-07-10 Wed 20:16:56>
#
# Thoughts: sort the list, from big to small. each time take one of
# `fresh' (non prviously picked) element, max, min, max, ... see if
# it fits a half of the two. if so place it, repeat using the other
#
# J. #247588

def split_into_half(lst, size):
    # create array of true, false for each emelemnt in the list
    has_picked = [False for e in lst]
    from_left = True
    halfs = [[], []]

    lst.sort(reverse=True)      # biggest on left
    if lst[0] > size:
        return []

    for i in range(len(lst)):
        if from_left:
            index = i
        else:
            index = len(lst) - i
        for half in halfs:
            if has_picked[index]:
                break
            elif not has_picked[index] and lst[index] + sum(half) <= size:
                half.append(lst[index])
                has_picked[index] = True
                from_left = from_left ^ True
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
