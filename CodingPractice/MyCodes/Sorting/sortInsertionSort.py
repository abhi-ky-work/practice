arr = [30,63,10,12,20,45,12,50,60,40]

# for i in range(1, len(arr)):
#     currentNumber = arr[i]
#     j = i
#     while currentNumber < arr[j-1] and j > 0:
#         arr[j] = arr[j-1]
#         j = j - 1
#     arr[j] = currentNumber
#     print("iteration : ",i , " array => " , arr)

# print("final : ",arr)




# docversion original
# for i in range ( 1, len(arr)):
# 	currentNumeber = arr[i]
# 	j = i
# 	while a[j] > a[j+1] and j >0:
# 		a[j] = a[j+1]
# 		J -= 1
# 	A[i] = currentNumber

for i in range ( 1, len(arr)):
	currentNumeber = arr[i]
	j = i 
	while currentNumeber < arr[j-1] and j >0:
		arr[j] = arr[j-1]
		j -= 1
	arr[j] = currentNumeber
print(arr)