class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        st = list(s)
        
        count = 0
        
        l = count*(2*k)
        p = min(l + 2*k - 1,len(st)-1)
        diff = p - l + 1
        if(diff==2*k):
            r = l + k - 1
        elif(diff>=k and diff<2*k):
            r = l + k - 1
        elif(diff<k):
            r = p
        
        while(l<len(st)):
            while(l<r):
                st[l], st[r] = st[r], st[l]
                l += 1
                r -= 1
            l = p + 1
            p = min(l+2*k-1,len(st)-1)
            diff = p - l + 1
            if(diff==2*k):
                r = l + k - 1
            elif(diff>=k and diff<2*k):
                r = l + k - 1
            elif(diff<k):
                r = p
                
        res = ''.join(st)
        
        return res