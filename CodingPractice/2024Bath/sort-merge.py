arr = [1, 3, 5, 2, 55, 22, 12, 34 ,26 , 64 , 36 , 54 , 32 , 34 ]



def merge_sort(arr):

    if len(arr)> 1:

        m = len(arr)//2

        left_arr = arr[ :m]
        right_arr = arr[m:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else :
                arr[k] = right_arr[j]
                j +=1
            k+=1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

merge_sort(arr)
print("Result => ", arr)