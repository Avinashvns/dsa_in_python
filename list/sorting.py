# selection sort
a = [2, 9, 1, 6, 7, 3]
n = len(a)
print(n)

for i in range(n):
    min = a[i]
    minpos = i
    for j in range(i+1, n):
        if a[j] < min:
            min = a[j]
            minpos = j
    a[i], a[minpos] = a[minpos], a[i]
    print("min value", a[i], "min Pos", a[minpos])

print(a)

# bubble sort
arr = [8, 9, 4, 2, 3, 25]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

print(arr)
