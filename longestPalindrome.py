
class Solution(object):
    def delta(self,s,lastp):
        l,start,end = 0,-1,-1
        longest = ''
        for i in range(1,lastp+1):
            if s[lastp] == s[lastp-i]:
                if i == 1 or i == 2:
                    self.cache.add( self.make_key(lastp-i,lastp))
                    start,end = lastp-i,lastp+1
                    l = i
                    continue
                elif self.make_key(lastp-i+1,lastp-1) in self.cache:
                    if self.make_key(lastp-i+1,lastp-1) in self.cache:
                        self.cache.add( self.make_key(lastp-i,lastp))
                        start,end = lastp-i,lastp+1
                        l = i
        if start >=0 and end >= 0:
            longest = s[start:end]
        return l,longest
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        self.cache = set()
        self.make_key = lambda x,y:x+y*10000
        if len(s) > 0:
            dp = [0] * len(s)
            dp[0] = 0
            longest = s[0]
            for i in range(1,len(s)):
                #print i
                newlongest,slongest = self.delta(s,i)
                #print i,newlongest,slongest
                if newlongest > dp[i-1]:
                    dp[i] = newlongest
                    longest = slongest
                else:
                    dp[i] = dp[i-1]
#         print self.cache
        return longest
    
if __name__ == '__main__':
    s = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    solver = Solution();
    print solver.longestPalindrome(s)