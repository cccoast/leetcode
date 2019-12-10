
class Solution(object):
    def dfs(self,start,cur_nums,target):
#         print self.cache,cur_nums,target
        s = ''.join([str(i) for i in cur_nums])
        if (s,target) in self.cache:
            return False
        if target == 0:
#             print start,cur_nums
            self.cache.add((s,target))
            self.values.append([i for i in cur_nums])
            return True
        for i in range(start,self.length):
            if self.candidates[i] <= target:
                cur_nums.append(self.candidates[i])
                ret = self.dfs(i+1,cur_nums,target - self.candidates[i])                    
                cur_nums.pop(-1)
                if ret:
                    self.cache.add((s,target))
                                    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.cache = set()
        self.values = []
        self.length = len(candidates)
        self.candidates = sorted(candidates)
        cur_nums = []
        self.dfs(0,cur_nums,target)
        return self.values
    
if __name__ == '__main__':      
    candidates = [10,1,2,7,6,1,5]
    target = 8
    solver = Solution()
    print solver.combinationSum2(candidates,target)
    