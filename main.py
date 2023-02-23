# task 26

def stepen(n, x):
    if x == 1:
        return n
    return n * stepen(n, x - 1)


print(stepen(5, 4))


# task 28


def sum_of(a, b):
    if a == 0:
        return b
    return sum_of(a - 1, b + 1)


print(sum_of(5, 10))
