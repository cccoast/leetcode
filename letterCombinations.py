class Solution(object):
    def dfs(self,sub,start):
        if start >= len(self.digits):
            self.group.append(sub)
            return 
        else:
            for alpha in self.dic[int(self.digits[start])]:
                self.dfs(''.join((sub,alpha)),start+1)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return ''
        self.digits = digits
        self.dic = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        self.group = []
        self.dfs('',0)
        return self.group
    
if __name__ == '__main__':
    s = "23"
    solver = Solution()
    print solver.letterCombinations(s)