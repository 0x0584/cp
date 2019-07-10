#              File:    azuz-n-treasure.py
#            Author:    Anas
#
#    Created: <2019-07-08 Mon 23:36:21>
#    Updated: <2019-07-10 Wed 08:42:05>
#
# Thoughts: the idea is that we have to collect a list of all possible
# paths, keeping tack of only new corridros. and keep going deeper using
# recursion until we reach a corridor with no next, we return the paths.
# finally, we'll have to check for traps.
#
# B. #247588

def find_next(corris, corr):
    lst = []
    for e in corris:
        if (e[0] == corr[1]):
            lst.append(e)
    return lst

def solve(corris, paths = [[[0, 1]]]):
    new_paths = []
    has_new_next = False

    l = list(paths)
    for path in paths:
        for e in find_next(corris, path[-1]):
            if e not in path:
                has_new_next = True
                new_paths.append(path + [e])
    if not has_new_next:
        return list(paths)
    return solve(corris, new_paths)

def treasure(solu):
    last_room = solu[0][-1][1]
    is_trap = False
    i = 0

    while i < len(solu):
        if solu[i][-1][1] != last_room:
            is_trap = True
            break
        i += 1

    if not is_trap:
        print last_room
    else:
        print "it was a trap!"

# def run_tests(fname):
#     index = 0
#     with open(fname) as f:
#         content = f.readlines()
#     content = [x.strip() for x in content]

#     for i in range(int(content[0])):
#         corris = []
#         index += 1
#         n_corris = int(content[index]) - 1
#         index += 1
#         for j in range(n_corris):
#             corris.append(map(int, content[j + index].split()))
#         index += j
#         treasure(solve(corris))


# run_tests("azuz.in")

n_tests = int(input())
input_arr = []
for i in range(n_tests):
    corris = []
    n_corris = int(input())
    for j in range(n_corris - 1):
        corris.append(map(int, raw_input().split()))
    input_arr.append(corris)
for e in input_arr:
    treasure(solve(e))
