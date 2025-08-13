'''
N house is a row with some value to steal 
theif cannot steal from two adjascent houses
what is the max value he can steal from these houses


approach:
he has has to start with first or second house,
if starts from 3rd, will get lesser bec one from first is also eligible


case 1 : starts with first house
case 2 : skips first and starts from second
'''


def max_money(arr, i):
    
    if i >= len(arr):
        return 0

    steal_curr_house = arr[i] + max_money(arr, i+2)
    skip_curr_house = max_money(arr, i + 1)
    return max( steal_curr_house, skip_curr_house)


arr = [20, 5, 1, 13, 6, 11, 40] # ans : 73
arr = [6, 7, 1, 30, 8, 2, 4] # ans : 41


print("Max thief steal is : ", max_money(arr, 0))