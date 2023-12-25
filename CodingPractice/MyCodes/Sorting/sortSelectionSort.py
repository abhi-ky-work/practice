arr = [30,63,10,12,20,45,50,60,40]

print(arr)
# for i in range( len(arr) ):
    
#     min=i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min]:
#             min = j

#     print("minIndex : ",min)
#     if( min != i):
#         temp = arr[i]
#         arr[i] = arr[min]
#         arr[min] = temp
#     print(arr)

# print("final : ", arr)


# doc version 
# For i in range( len(arr) - 1 ):
# 	iMin = i
# 	For j in range( i +1, len(arr)):
# 		If a[j] < a[imin] :
# 			Imin = j
# 	If imin != j :
# 		A[imin],a[j] = a[j], a[imin]

# print(arr)

for i in range( len(arr)):
	imin = i
	for j in range( i +1, len(arr)):
		if arr[j] < arr[imin] :
			imin = j
	if imin != i :
		arr[imin],arr[i] = arr[i], arr[imin]

print(arr)
