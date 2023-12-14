#因為是淘汰賽，n隊的話，只要比n-1場就可以淘汰其他隊伍，就得冠軍
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1