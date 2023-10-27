# 1 2 4 8 16 32 64 128 256...
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0: return False #如果沒有這一行，n是負的或是0，就錯了
        while n>1: #因為1是2的0次方，就不用再繼續除了
            if n%2 != 0: #竟然餘數不是0
                return False #失敗
            n = n//2
        # 經過樓上檢查，都沒有出錯的話
        return True #就是成功