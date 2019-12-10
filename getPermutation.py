class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        a = [ str(i) for i in range(1,n+1)]
        v = [1] * (n + 1)
        for i in range(1,n + 1):
            v[i] = i * v[i-1]
        p = n-1
        print v
        s = []
        k -= 1
        while k > 0:
            print k,' ',
            i,j = k/v[p],k%v[p]
            p -= 1
            k = j
            s.append(i)
        print ''
        print s
        ret = []
        for i in s:
            ret.append(a[i])
            del a[i]
        for i in a:
            ret.append(i)
        return ''.join(ret)
    
if __name__ == '__main__':
    n,k = 1,1
    solver = Solution()
    print solver.getPermutation(n, k)