#              File:    little-a.py
#            Author:    Anas
#
#    Created: <2019-07-10 Wed 09:49:31>
#    Updated: <2019-07-10 Wed 09:57:55>
#
# Thoughts: a kind of off-by-one problem. size++ if n % limit
#
# M. #247588

LIMIT = 50

def get_count_containers(n_candies):
    assert 1 <= n_candies <= 1e5
    size = int(n_candies / LIMIT)
    if (n_candies % LIMIT != 0):
        size += 1
    return size

print get_count_containers(int(input()))
