s1 = 'tcable'
s2 = "tgable"




def convertString(s1,s2, l1, l2):
    if l1 == len(s1):
        return len(s2) - l2

    if l2 == len(s2):
        return len(s1) - l1

    if s1[l1] == s2[l2] :
        return convertString(s1, s2, l1 + 1 , l2 + 1)

    c1 = 1 + convertString(s1, s2, l1+ 1 , l2) # inserting char in s1
    c2 = 1 + convertString(s1, s2, l1 , l2 + 1 )#deleting char from s1
    c3 = 1 + convertString(s1, s2, l1 + 1, l2 + 1) # replacing char in s1
    return min(c1, c2, c3 )


step = convertString(s1, s2, 0, 0)
print(step)