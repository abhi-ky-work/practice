arr = [30, 10, 50, 20, 40, 70, 60,40, 80]


def insertion_sort(arr):

    for j in range(1, len(arr)):
        i = j
        while i > 0 and arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i] , arr[i-1]
            i -= 1
    print(arr)
insertion_sort(arr)