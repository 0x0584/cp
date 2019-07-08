def last_digit(k, a, n):
    result = 0
    for i in range(1, n):
        result = (a * result) % 10**k
    return result

n_tests = input()
arr = []
for i in range(0, n_tests):
    arr.append(input())           # a
    arr.append(input())           # n
    arr.append(input())           # k

for i in range(0, len(arr) / 3):
    s = 0
    for c in str(last_digit(arr[i], arr[i + 1], arr[i + 2])):
        print c, "  ", int(c)
        s = s + int(c);
    print s
