class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re 
        star = re.compile('(\*)+')
        p = re.sub(star,'*',p)
        p = p.replace('*','(\w)*')
        p = p.replace('?','(\w)')
        print p
        pattern = re.compile(p)
        obj = re.match(pattern,s)
        if obj:
            return obj.group() == s 
        return False
    
    
if __name__ == '__main__':
    s,p = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba","*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
    solver = Solution()
    print solver.isMatch(s, p)