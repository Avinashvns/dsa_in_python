# Question

# Sort a Python list based on number of 0s in a numbered list.
# a=[100,2,101]
# sorted list =[2,101,100]


# Solve

# def f(n):
#     n = str(n)
#     count = 0
#     for x in n:
#         if x == "0":
#             count += 1
#     return count


# num1 = [1, 200, 5, 20, 5000]
# print(num1)
# data = sorted(num1)
# # data.sort(key=f)
# print(data)


# Sort a Python list of numbers based on odd or even. Odd numbers will come first.
# a=[11,2,34,60,33,45]
# sorted list=[11,33,45,2,34,60]

# numlist = [9, 6, 5, 8, 1, 4, 2, 7]


# def odd(n):
#     if n % 2 != 0:
#         return "a" + str(n)
#     return "b" + str(n)


# newnum = sorted(numlist, key=odd)
# print(newnum)


# Sort a Python list of 3 number Tuples based on their sum.
# a=[(1,2,3),(1,1,1),(2,5,4),(0,1,0)]
# sorted list=[(0,1,0),(1,1,1),(1,2,3),(2,5,4)]

# a = [(1, 2, 3), (1, 1, 1), (2, 5, 4), (0, 1, 0)]

# def f(n):
#     print(n)
#     n = sum(n)
#     # total = 0
#     # for x in n:
#     #     total += x
#     # print(total)
#     # return total
#     print(n)
#     return n

# a.sort(key=f)
# print(a)

# Sort a list of date tuples.
# a=[(19,3,2022),(16,1,1970),(15,8,1947),(31,12,1946)]
# sorted list=[(31,12,1946),(15,8,1947),(16,1,1970),(19,3,2022)]

a = [(19, 3, 2022), (6, 1, 1970), (15, 8, 1946), (31, 12, 1946)]
# 19470815


def f(n):
    # print(n[2], "and", n[1])
    day, month, year = n
    if day < 10:
        day = "0"+str(day)
    else:
        day = str(day)

    if month < 10:
        month = "0"+str(month)
    else:
        month = str(month)

    year = str(year)
    n = year+month+day

    print(day, month, year)
    print("Day: ", n)

    return n


a.sort(key=f)
print(a)


a = [1, 5, 3, 9]
n = len(a)
for i in range(n):
    min, minpos = a[i], i
    for j in range(i+1, n):
        if a[j] < min:
            min = a[j]
            minpos = j
    a[i], a[minpos] = a[minpos], a[i]
print(a)
