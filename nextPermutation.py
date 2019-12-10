
class multi_set(list):
    def __init__(self):
        super(multi_set,self).__init__()
    def add(self,v):
        for index,_v in enumerate(self):
            if _v >= v:
                self.insert(index,v)
                return 
        self.append(v)
    
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        candidate = multi_set()
        for i in range(len(nums))[::-1]:
            candidate.add(nums[i])
            print i,candidate
            if len(candidate) > 0:
                can_return = False
                for v in candidate:
                    if v > nums[i]:
                        nums[i] = v
                        candidate.remove(v)
                        can_return = True
                        break
                if can_return:
                    index = i + 1
                    for v in candidate:
                        nums[index] = v
                        index += 1
                    return
        for index,v in enumerate(sorted(nums)):
            nums[index] = v
            

if __name__ == '__main__':      
    nums = [2,2,7,5,4,3,2,2,1]
    solver = Solution()
    solver.nextPermutation(nums)
    print nums
#     s = multi_set()
#     for i in range(10)[::-1]:
#         s.add(i)
#     print s