'''
Given a num
count the number of ways to express N as sum of 1, 3, 4 


wtg 0 => 1
wtg 1 => 1
wtg 2 => 1
wtg 3 => 2 [wtg 2, wtg 0]

wtg 4 => 4, 1-3, 3-1, 1-1-1-1

wtg 8 => 
wtg 7 [wtg 6 , wtg 4 , wtg 3], wtg 5 [wtg 4 , wtg 2 , wtg 1] , wtg 4 [wtg 3 , wtg 1 , wtg 0]



gpt:
ways(0) = 1

ways(1) = ways(0) = 1

ways(2) = ways(1) = 1

ways(3) = ways(2) + ways(0) = 1 + 1 = 2

ways(4) = ways(3) + ways(1) + ways(0) = 2 + 1 + 1 = 4

ways(5) = ways(4) + ways(2) + ways(1) = 4 + 1 + 1 = 6

ways(6) = ways(5) + ways(3) + ways(2) = 6 + 2 + 1 = 9

ways(7) = ways(6) + ways(4) + ways(3) = 9 + 4 + 2 = 15

ways(8) = ways(7) + ways(5) + ways(4) = 15 + 6 + 4 = 25

ways(9) = ways(8) + ways(6) + ways(5) = 25 + 9 + 6 = 40

ways(10) = ways(9) + ways(7) + ways(6) = 40 + 15 + 9 = 64

'''

def ways_to_get_num(num):

    if  num <= 2:
        return 1
    if num == 3:
        return 2
    if num == 4:
        return 4

    w1 = ways_to_get_num(num - 1)
    w2 = ways_to_get_num(num - 3)
    w3 = ways_to_get_num(num - 4)

    return w1 + w2 + w3

num = 10

print("Ways to get num of ", num , " is : ", ways_to_get_num(num))