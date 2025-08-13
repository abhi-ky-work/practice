demoniations = [1, 5, 10, 50, 100, 500]
amount = 45332


def coin_change(amount, arr):
    count = 0
    i = len(arr) -1
    val = amount
    while i >= 0 and val != 0:
        count += val // arr[i]
        val = val % arr[i]
        i -= 1
        print( val, count)
    print(count)

'''
given an amount
of which want to make changes for this amount
provided infinite amount of supply of coins of each denominations in indian currency

what is the minimum number of coins required to make the change


appraoch:
sort the list of denominations in desc order
use the max no of highest denominatins 
and then go for next highest dnominations


'''
coin_change(amount, demoniations)

