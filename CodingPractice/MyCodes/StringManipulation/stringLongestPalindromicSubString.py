s1 = "mamdrdm"




# def find_longest_palindromic_sub_string(s1,si, li):
#     if si > li:
#         return 0
#     if si == li : 
#         return 1
    
#     c1 = 0
#     if s1[si] == s1[li]:
#         if s1[si+1] == s1[li-1]:
#             c1 = 2 + find_longest_palindromic_sub_string(s1, si+ 1, li -1)

#     c2 = find_longest_palindromic_sub_string(s1, si+1,li)
#     c3 = find_longest_palindromic_sub_string(s1, si,li-1)

#     return max(c1, c2, c3)
    
# print(find_longest_palindromic_sub_string(s1, 0, len(s1) - 1))

def find_longest_palindromic_sub_string(s1,si, li):
    if si > li:
        return 0
    if si == li : 
        return 1
    
    c1 = 0
    if s1[si] == s1[li]:
        remaining_length = li -si -1
        if remaining_length == find_longest_palindromic_sub_string(s1, si+1,li-1):
            c1 = remaining_length + 2

    c2 = find_longest_palindromic_sub_string(s1, si+1,li)
    c3 = find_longest_palindromic_sub_string(s1, si,li-1)

    return max(c1, max(c2, c3))
    
print(find_longest_palindromic_sub_string(s1, 0, len(s1) - 1))