class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        #先把week08-3 的倆倆比較寫出來
        N = len(arr) #小心，題目不是 a 而是 arr

        for k in range(N):
            for i in range(1,N):
                if arr[i]<arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]

        for i in range(1,N):
            if arr[i] - arr[i-1] != arr[1] - arr[0]:
                return False
        return True