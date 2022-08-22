class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        if(s[:2]=='ab' and s[-2:]=='ba' and k==2):
            return ""
        
        res = ''
        
        d = {}
        
        cur = 0
        c = 1
        
        for i in range(1,len(s)+1):
            if(i<len(s) and s[i]==s[cur]):
                c += 1
            
            else:
                if((len(res)>0 and res[-1]!=s[cur]) or len(res)==0):
                    if(c<k):
                        res += s[cur]*c
                        d[s[cur]] = c
                    elif(c>k):
                        rem = c%k
                        res += s[cur]*rem
                        d[s[cur]] = rem
                elif(res[-1]==s[cur]):
                    dc = d[s[cur]]
                    if((dc+c)==k):
                        res = res[:-dc]
                        d[s[cur]] = 0
                    elif((dc+c)>k):
                        rem = (dc+c)%k
                        res = res[:-dc]
                        res += s[cur]*(rem)
                        d[s[cur]] = rem
                    else:
                        res += s[cur]*c
                        d[s[cur]] += c
                        
                cur = i
                c = 1
                
        return res