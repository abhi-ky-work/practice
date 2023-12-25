s1 = "houdini"
s2 = "hdupti"



def find_longest_sub_seq(s1,s2,l1,l2):
    if (len(s1) == (l1)) or (len(s2) == (l2)):
        return 0
    else:
        # print("Length : ", l1, l2)
        c1 = 0
        if s1[l1] == s2[l2]:
            c1 = 1 + find_longest_sub_seq(s1,s2, l1 + 1, l2 + 1)

        
        c2 = find_longest_sub_seq(s1,s2,l1 + 1, l2 + 1)
        c3 = find_longest_sub_seq(s1, s2, l1, l2+ 1)
        return max(c2, c3, c1)

print(find_longest_sub_seq(s1,s2,0, 0) )