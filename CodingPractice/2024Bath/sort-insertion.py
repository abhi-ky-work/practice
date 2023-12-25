
arr = [1, 3, 5, 2, 55, 22, 12, 34 ,26 , 64 , 36 , 54 , 32 , 34 ]



for i in range(len(arr)):
    currNum = arr[i] # jo item uthaya from unsorted array save as temp
    j = i
    while j > 0 and currNum < arr[j-1]: # jab tak tab tak piche wala element temp wale se chota nahi mil jata 
        arr[j] = arr[j-1] # agar piche walw chota hai temp se to age shift kar diya
        j -=1 # then shifted to the one element back
    arr[j] = currNum # jo temp uthaya tha usko waha daal diya jaha uske piche wala usse chota mil gaya 

print(arr)