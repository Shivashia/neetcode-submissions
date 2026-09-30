class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:
            if s[l]!=s[r]:
                lef=s[l+1:r+1]
                rig=s[l:r]
                return lef == lef[::-1] or rig == rig[::-1]
            l+=1
            r-=1        
        return True