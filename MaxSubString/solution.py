def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    hSet={}
    maxSub=0
    runningMax=0
    i = 0
    while i != len(s):
        if s[i] not in hSet: 
            runningMax += 1
            hSet[s[i]]=True
        else:
            hSet = {}
            if maxSub < runningMax:
                maxSub = runningMax
            runningMax = 0
            restIndex = i
            while restIndex > 0 and s[i] != s[restIndex-1]:
                restIndex-=1
            
            if restIndex == 2:
                break
            i = restIndex
            continue          
        i += 1
    if maxSub < runningMax:
        maxSub = runningMax

    return maxSub      

if __name__ == "__main__":
    print(lengthOfLongestSubstring("aab"))