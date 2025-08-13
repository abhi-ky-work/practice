arr = [30, 10, 50, 20, 40, 70, 60,40, 80]


def selection_sort(arr):
    
    for j in range(len(arr)):
        imin = j 
        for i in range(j+1, len(arr)):
            if arr[i] < arr[imin]:
                imin = i 
        if imin != j:
            arr[imin], arr[j] = arr[j], arr[imin]
    print(arr)

    
selection_sort(arr)