
class Solution(object):
    
    def fill(self,index,v,lastp,length):
        if index == length:
            self.results.append([i for i in v])
        elif index < length:
            for i in range(lastp,len(self.nums)):
                v.append(self.nums[i])
                self.fill(index + 1,v,i+1,length)
                v.pop(-1)
    
    def get_length_n(self,length):
        v = []
        self.fill(0,v,0,length)
                
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.results = []
        for i in range(len(nums)+1):
            self.get_length_n(i)
        return self.results

if __name__ == '__main__':
    nums = [1,2,3]
    solver = Solution()
    print solver.subsets(sorted(nums))