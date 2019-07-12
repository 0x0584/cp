#              File:    omar-n-puzzle.py
#            Author:    Anas
#
#    Created: <2019-07-11 Wed 20:08:07>
#    Updated: <2019-07-12 Fri 11:39:02>
#
# Thoughts: loop over the points, each time, push a point into a range r
# if the range still has space, and the diff is true. mark the point as
# picked. loop over again.
#
# H. #247588

def diff(lst, k):
    if not lst or len(lst) == 0:
        return False
    elif len(lst) == 1:
        return True
    for e1 in lst:
        for e2 in lst:
            if e2 - e1 > k:
                return False
    return True

def range_of_points(points, c, k):
    picked = [False for e in points]
    ranges = [[]]
    flag = True

    ranges[0].append(points[0])
    picked[0] = True
    while flag:
        flag = False
        points[:] = [points[i] for i in range(len(points))
                     if not picked[i]]
        picked[:] = [e for e in picked if not e]
        for i in range(len(points)):
            if not picked[i]:
                flag = True
                for r in ranges:
                    if len(r) < c and diff(r + [points[i]], k):
                        picked[i] = True
                        r.append(points[i])
                        break
                if not picked[i]:
                    ranges.append([])
                    ranges[-1].append(points[i])
                    picked[i] = True
    return ranges

def run_tests():
    n_tests = int(input())
    tests = []
    for t in range(n_tests):
        tests.append([map(int, raw_input().split()), # reading N, C and K
                      map(int, raw_input().split())])
    for t in tests:
        print len(range_of_points(t[1], t[0][1], t[0][2]))

run_tests()
