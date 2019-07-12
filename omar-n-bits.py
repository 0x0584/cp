#              File:    omar-n-bits.py
#            Author:    Anas
#
#    Created: <2019-07-12 Fri 11:17:25>
#    Updated: <2019-07-12 Fri 11:33:35>
#
# Thoughts: find one bits using >> and & operators. split the number
# of powers of ten, then count bits in each one then return the max
#
# L. #247588

def count_bits(num):
    counter = 0
    while num != 0:
        if num & 1:
            counter += 1
        num = num >> 1
    return counter

def get_ten_pows(num):
    digits = map(int, str(num))
    ten_pows = []
    ten_pow = 1

    for d in reversed(digits):
        ten_pows.append(num / ten_pow)
        ten_pow *= 10
    return ten_pows

def max_one_bits(num):
    ten_pows = get_ten_pows(num)
    count = []

    for n in ten_pows:
        count.append(count_bits(n))
    return max(count)

def run_tests():
    n_tests = int(input())
    tests = []
    for t in range(n_tests):
        tests.append(int(input()))
    for t in tests:
        print max_one_bits(t)

run_tests()
