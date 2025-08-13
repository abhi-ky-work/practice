'''
Given two strings word1 and word2, return the count of minimum number of operations required to convert word2 to word1.
by deleting, inserting, or replacing a character.

'''
s1 = "catch"
s2 = "carch"  # ans 1 

s1 = "horse"
s2 = "ros"    # ans 3

s1 = "table"
s2 = "tgable"  # ans 1 




l1 = len(s1)
l2 = len(s2)
def find_min_operations(s1,s2, i1, i2):

    if i1 == l1 - 1:
        return l2 - (i2 + 1)
    if i2 == l2 - 1:
        return l1 - (i1 +1)
    
    if s1[i1] == s2[i2]:
        return find_min_operations(s1, s2, i1 + 1, i2 + 1)
    
    c1  = 1 + find_min_operations(s1, s2, i1 + 1 , i2) #insertion in s1
    c2  = 1 + find_min_operations(s1, s2, i1 , i2 + 1) # deletion in s2
    c3  = 1 + find_min_operations(s1, s2, i1 + 1 , i2 + 1) # replace in s2, s1


    return min(c1, c2, c3)

print("Mind operation to convert \n ", s2, " -> ", s1, " is : ", find_min_operations(s1, s2, 0 , 0))





    
    



