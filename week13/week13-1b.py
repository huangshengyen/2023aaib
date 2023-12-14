class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
       #return ''.join(word1) == ''.join(word2) #第二種寫法
        #以下為第一種寫法
        a = ''.join(word1)
        b = ''.join(word2)

        if a==b: return True
        else: return False