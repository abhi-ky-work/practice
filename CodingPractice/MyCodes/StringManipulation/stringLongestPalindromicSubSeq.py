s1 = "elrmenmet"
# s2 = "ememe"



def find_longest_palindromic_subseq(s1,si, li):
    if si > li:
        return 0
    if si == li:
        return 1
    
    c1 = 0 
    if s1[si] == s1[li]:
        c1 = 2 + find_longest_palindromic_subseq(s1,si + 1, li -1)

    c2 = find_longest_palindromic_subseq(s1, si+1, li)
    c3 = find_longest_palindromic_subseq(s1, si, li-1)
    return max(c1, c2, c3)

print(find_longest_palindromic_subseq(s1,0, len(s1)-1))
