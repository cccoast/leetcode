# 
# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) <= 1:return True
#         dp = [False for i in range(len(nums))]
#         dp[-1] = True
#         for i in range(len(nums)-1)[::-1]:
# #             print i,dp
#             for j in range(1,nums[i]+1):
#                 if i + j < len(nums):
#                     if dp[i+j] is True:
#                         dp[i] = True
#                         break
#         return dp[0]

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:return True
        least = len(nums) - 1
        for i in range(len(nums)-1)[::-1]:
            if least - i <= nums[i]:
                least = i
        return True if least == 0 else False
            
if __name__ == '__main__':
    nums = [2,3,1,1,4]
    solver = Solution()
    print solver.canJump(nums)