# 4 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # top sol
        
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

        # my sol 
        # dic = {}
        # for num in nums:
        #     if not dic.get(num, False) :
        #         dic[num] = True
        #     else:
        #         return True
        # return False
