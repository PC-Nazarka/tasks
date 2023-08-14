def binary_search(seq, value):
    l, r = 0, len(seq) - 1
    while l <= r:
        m = (l + r) // 2
        if seq[m] == value:
            return m
        if seq[m] > value:
            r = m - 1
        else:
            l = m + 1
    return -1

numbers = list(range(1, 11))
print(binary_search(numbers, 9))
