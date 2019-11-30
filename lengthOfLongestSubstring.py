class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        longest = 1
        i,right   = 0,0
        while i < len(s) and right < len(s):
            repeat = False
            for k in range(i,right):
                if s[k] == s[right]:
                    repeat = True
                    break
            if not repeat:
                longest = right-i+1 if right-i+1 > longest else longest
                right += 1
                continue
            i += 1
            right = i if i >= right else right
        return longest
                

if __name__ == '__main__':
    s = "siljapsqtvuilycxcajbdtxokfqzhwfbfslhhfxabtlmspkuptyuoxiacyzjxhlezylhdkj"
    solver = Solution()
    print solver.lengthOfLongestSubstring(s)

