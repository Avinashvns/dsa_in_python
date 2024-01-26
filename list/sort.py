# Sorting with Function

a = ["cat", "dog", "ball", "apple"]


def lastChar(s):
    print(s)
    # return s[len(s)-1]
    return s[-1]


a.sort(key=lastChar)
print(a)
