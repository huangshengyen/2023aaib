class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mother = "aeiouAEIOU"
        N=len(s) #字串長度ex: s="textbook" 
        count = 0
        for i in range(N):
            if i<N//2 and s[i] in mother: count+=1
            if i>=N//2 and s[i] in mother: count-=1
        if count == 0:return True
        else: return False
        