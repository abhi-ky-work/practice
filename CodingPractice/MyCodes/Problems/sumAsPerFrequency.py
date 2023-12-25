'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

inputs = [ i for i in list(map( str, inputs.split('\n') ))]
del(inputs[0], inputs[len(inputs) -1 ])

from collections import defaultdict
'''

# Write your code here
import sys
input = sys.stdin.readline
n = int(input())
inputs = input()
arr = [ i for i in list(map( int , inputs.split(' ') ))]
# print(arr)
from collections import Counter
dic = {}

for i in arr:
    # print(i,"in array")
    key = i
    finding = dic.get( key, "null" )
    if (finding == "null"):
        dic.update({key : 1})
    else:
        item = dic.get(key, 0 )
        # print(item , " : item")
        dic.update({ key : item + 1 })


# arr2 = dic.items()

valArr = [0]*(n+1)
# print(dic.items() )

for key,val in dic.items():
    valArr[val] += key*val

for i in range(1, n+1 ):
    valArr[i] += valArr[i-1]
# print("final array", valArr)
q = int( input() )
for t in range( q ):
    lr = input()
    # print( lr )
    l,r =(map(int, lr.split()))

    # arr2.sort()
    print( valArr[r]-valArr[l-1])
    
    



    # sum = 0
    # for j,i in arr2:
    #     if i >= l and i <= r:
    #         # print(sum, j*( dic.get(j, None ) ) )
    #         sum = sum + j*( dic.get(j, None ) )
    #     else:
    #         pass
    # print(sum)
    


# ========================================================

import sys
from collections import Counter
input = sys.stdin.readline
 
def solve():
    pass
 
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
f = [0]*(n+1)
for k, val in c.items():
    f[val] += val*k
for i in range(1, n+1):
    f[i] += f[i-1]
 
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(f[r]-f[l-1])
 
 