class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s) #長度
        zero = 0
        one = 0 #想找出全部的1
        for i in range(N):
            if s[i]=='1': one += 1 #如果是1，先全部加起來
        #現在就知道共有幾個 one
        ans = 0
        for i in range(N-1):#要逐格去做修正，「吐出」一格，看他是多少，就修正
            if s[i] == '0': #吐出'0' 給左邊
                zero += 1 #左邊多1個0
            if s[i] == '1': #吐出'1' 給左邊，右邊就少了1個'1'
                one -= 1  #右邊少1個1
            ans = max(ans, zero+one)
        return ans