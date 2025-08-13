'''
we are given two strings s1 and s2
find the longest common subsequence between them
the subsequence is not necessarily contiguous, but the order of characters should be maintained
the length of the longest common subsequence is returned 

'''

def longest_common_subsequence(s1, s2, i1, i2):

    if i1 == len(s1) or i2 == len(s2):
        return 0
    c1 = 0
    if s1[i1] == s2[i2]:
        c1 = 1 + longest_common_subsequence(s1, s2, i1 + 1, i2 +1)
    c2 = longest_common_subsequence(s1, s2 , i1 + 1, i2)
    c3 = longest_common_subsequence(s1, s2, i1, i2 +1)

    return max(c1, c2, c3)


s1 = 'elephant'
s2 = 'erehpant'  # ans 6
# s2 = 'ereptat'  # ans 5

s1 = 'houdini'
s2 = 'hdupti'


print("Longest common subsequence length is : ", longest_common_subsequence(s1, s2, 0, 0))