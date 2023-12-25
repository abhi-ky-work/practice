arr = [30,63,10,12,20,45,99,22,50,60,40]

# def quick_sort(arr,q,p):
#     print("Prama : ", q, " ", p)
#     if q < p:
#         r = partition(arr,q, p)
#         quick_sort(arr,q, r-1)
#         quick_sort(arr, r+1, p )


# def partition(arr, q, p):

#     pivot = p
#     i = q-1

#     for j in range(q, p+1):
#         if arr[j] <= arr[p]:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     # arr[i+1], arr[p] = arr[p], arr[i+1]
        
#     return i


# quick_sort(arr,0,len(arr)-1)

# print("Final Sorted Array", arr)



# doc version

def quick_sort(arr, l, r ):
	if l < r : 
		p  = partition(arr,l ,r)
		quick_sort(arr,l, p-1)
		quick_sort(arr,p+1,r)

def partition(arr,q,p):
    i=q-1
    pivot = arr[p]
    for j in range(q, p+1):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    return i

	

quick_sort(arr, 0 , len(arr)-1)
print(arr)