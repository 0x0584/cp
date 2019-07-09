#              File:    azuz-n-treasure.py
#            Author:    Anas
#       Description:    finding the path through the treasure, which is
#                       the deepest room
#
#         Created: <2019-07-08 Mon 23:36:21>
#         Updated: <2019-07-09 Tue 02:29:25>
#
# B. #247588

def find_next(corris, corr):
    lst = []
    for e in corris:
        if (e[0] == corr[1]):
            lst.append(e)
    return lst

final_paths = []
def solve(corris, paths = [[[0, 1]]]):
    new_paths = []
    has_new_next = False

    for p in paths:
        for e in find_next(corris, p[-1]):
            if e not in p:
                has_new_next = True
                p.append(e)
                print " p >> ", p
                new_paths.append(p)
                print "new paths: ", new_paths

    if not has_new_next:
        final_paths.append(new_paths)
    else:
        solve(corris, new_paths)

corris = [
    [1, 2],
    [1, 3],
    [2, 3],
    [3, 4],
    [1, 5]
]

print corris
solve(corris)
print "final", final_paths

# start at index 1
# find next rooms
# got to each next room
#
