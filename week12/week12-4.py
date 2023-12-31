class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ans = 0 #迴圈前面=0
        while n>0: #剝皮法，一次剝一層皮(第07週)
            ans += n%2 #撥下來的屑屑收集起來
            n = n // 2 #洋蔥剝皮後，變小了
        return ans #迴圈後面 ans 拿來用