

def fibbonacci_divide_conquer(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    else:
        return fibbonacci_divide_conquer(num-1) + fibbonacci_divide_conquer(num-2)
    


num = 9
print("Fibbonacci Num Of ", num , " is : ", fibbonacci_divide_conquer(num))



'''
We’ll assume F(1) = 0, F(2) = 1 (some people start with 1, 1 — but I’ll use the most common in programming/math).

1  F(1) = 0
2  F(2) = 1
3  F(3) = 1 (0 + 1)
4  F(4) = 2 (1 + 1)
5  F(5) = 3 (1 + 2)
6  F(6) = 5 (2 + 3)
7  F(7) = 8 (3 + 5)
8  F(8) = 13 (5 + 8)
9  F(9) = 21 (8 + 13)
10 F(10) = 34 (13 + 21) ✅

So, the 10th number in the Fibonacci series is 34 if we start at 0.

If you start the series at 1, 1 instead, the 10th term would be 55.

'''