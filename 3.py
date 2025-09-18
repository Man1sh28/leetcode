class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        l1=[]
        for i in s:
            if i not in l1:
                l1.append(i)
            else:
                maxi = max(maxi, len(l1))
                l1 = l1[l1.index(i)+1:]
                l1.append(i)
        maxi = max(maxi, len(l1))
        
        return (maxi)