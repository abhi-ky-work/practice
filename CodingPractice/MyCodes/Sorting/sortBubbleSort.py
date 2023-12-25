# arr = [30,63,10,12,20,45,50,60,40]



# for i in range( len(arr) -1 ):
#     for j in range( len(arr) - i -1):
#         if arr[j] > arr[j+1]:
#             temp = arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1] = temp

# print(arr)



arr = [4,5,6,7,8,92,3,4,6,77]

for i in range(len(arr)-1):
	for j in range(len(arr)-i-1):
		if arr[j] > arr[j+1]:
			arr[j] , arr[j+1] = arr[j+1], arr[j]

print(arr)
