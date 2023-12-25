

arr = [1, 3, 5, 2, 55, 22, 12, 34 ,26 , 64 , 36 , 54 , 32 , 34 ]


for i in range(len(arr)):
    imin = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[imin]:
            imin = j
    if imin != i:
        arr[imin] , arr[i] = arr[i], arr[imin]


print(arr)