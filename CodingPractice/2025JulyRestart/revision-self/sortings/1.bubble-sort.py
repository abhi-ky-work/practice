arr = [30, 10, 50, 20, 40, 70, 60,40, 80]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


bubble_sort(arr)