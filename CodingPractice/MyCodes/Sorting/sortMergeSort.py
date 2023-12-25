arr = [30,63,10,12,20,63,45,50,60,40,99]


def merge_sort(arr):

    if len(arr) == 1:
        return

    mid = len(arr)//2

    left_array = arr[:mid]
    right_array = arr[mid:]

    merge_sort(left_array)
    merge_sort(right_array)

    i = 0 
    j = 0 
    k = 0 

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1

        k += 1

    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1

merge_sort(arr)
print(arr)




# ==============================

# def merge_sort(arr,l,r):
#     mid = (l+r-1)//2
#     if r > l:
#         merge_sort(arr,l,mid)
#         merge_sort(arr,mid+1,r)
#         merge(arr, l , mid , r)


# def merge(arr, l , m , r):
#     n1 = m -l +1
#     n2 = r-m
#     left_arr = [0]*n1
#     right_arr = [0]*n2

#     for i in range(0,n1):
#         left_arr[i] = arr[l + i]

#     for j in range(0, n2):
#         right_arr[j] = arr[m + 1 + j]

#     # print(arr, " => ", left_arr , " : ", right_arr)

#     i = j = 0
#     k = l
#     # print("length of L and R ", len(left_arr), " ", len(right_arr))
#     while i < n1 and j < n2:
#         if left_arr[i] <= right_arr[j]:
#             arr[k] = left_arr[i]
#             i += 1
#         else:
#             arr[k]=right_arr[j]
#             j += 1
#         k += 1

#     while i < n1: 
#         arr[k] = left_arr[i]
#         i +=1
#         k +=1

#     while j < n2:
#         arr[k] = right_arr[j]
#         j += 1
#         k += 1


# merge_sort(arr, 0, len(arr)-1)

# # merge([99,30],0,1,2)

# print("final array", arr)
