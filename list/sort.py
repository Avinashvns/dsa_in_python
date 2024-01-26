# Sorting with Function of compare

import functools as ft


def mycompare(a, b):
    print(a, b)
    if a % 2 == 0:
        return 1
    if b % 2 == 0:
        return -1
    return 0

    # return b-a


a = [1, 2, 3, 4, 5]
a.sort(key=ft.cmp_to_key(mycompare))
print(a)


# b-a ==0
# b-a gretharthan
