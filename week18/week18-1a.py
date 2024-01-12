class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        motherA=0 #a的母音有幾個
        motherB=0 #b的母音有幾個
        N=len(s) #字串長度ex: s="textbook"
        a = s[:N//2]#前半段 a="text"
        b = s[N//2:]#後半段 b="book"
        for c in a: #在a裡面的每一個字母c逐一檢查
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u': # 小寫母音
                motherA+=1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U': # 大寫母音
                motherA+=1
        for c in b:#在b裡面的每一個字母c逐一檢查
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':# 小寫母音
                motherB+=1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':# 大寫母音
                motherB+=1
        if motherA == motherB: return True
        else: return False