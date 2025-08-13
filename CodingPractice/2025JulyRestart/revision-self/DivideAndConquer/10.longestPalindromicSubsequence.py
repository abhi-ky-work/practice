
def longest_palindromic_subseq(s,l, r):
    if l> r :
        return 0
    
    if r == l:
        return 1

    c1 = 0
    if s[l] == s[r] and l <= r:
        c1 = 2 + longest_palindromic_subseq(s, l+1, r-1)
        # print(s[l])

    c2 = longest_palindromic_subseq(s, l+1, r)
    c3 = longest_palindromic_subseq(s, l, r-1)

    return max(c1, c2, c3)

s = 'ameewmea' # 6
s = 'elrmenmet' # 5
print("Length of the palindrome is ", longest_palindromic_subseq(s, 0, len(s)-1))