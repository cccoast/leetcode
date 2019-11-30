class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re 
        pattern = re.compile(p)
        obj = pattern.match(s)
        print obj
        if obj:
            return True if obj.group() == s else False
        return False
    
if __name__ == '__main__':
    s,p = 'aa','a'
    solver = Solution()
    print solver.isMatch(s, p)