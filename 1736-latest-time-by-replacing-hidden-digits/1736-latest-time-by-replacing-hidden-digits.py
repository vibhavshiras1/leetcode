class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        res = ""
        i = 0
        
        while(i<len(time)):
            if(time[i]=='?'):
                if(i==0):
                    if(time[i+1]=='?'):
                        res += str(23)
                    elif(int(time[i+1])<=3):
                        res += str(2)
                        res += time[i+1]
                    elif(int(time[i+1])>3):
                        res += str(1)
                        res += time[i+1]
                    i += 2
                elif(i==1):
                    if(time[i-1]=='0'):
                        res += str(9)
                    if(time[i-1]=='1'):
                        res += str(9)
                    elif(time[i-1]=='2'):
                        res += str(3)
                    i += 1
                elif(i==3):
                    if(time[i+1]=='?'):
                        res += str(59)
                    else:
                        res += str(5)
                        res += time[i+1]
                    i += 2
                elif(i==4):
                    res += str(9)
                    i += 1
                
            else:
                res += time[i]
                i += 1
                
        return res