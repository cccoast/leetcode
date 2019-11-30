class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        can_used = set()
        for i in range(len(nums))[::-1]:
            

if __name__ == '__main__':      
    solver = Solution()
    print solver.nextPermutation()