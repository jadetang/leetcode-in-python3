class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
      #  @lru_cache(None)
        def score(s):
            print(s)
            if 'ab' not in s and 'ba' not in s:
                return 0
            for i in range(0, len(s) - 2):
                if s[i: i + 3] == 'aba':
                    if x >= y:
                        return x + score(s[0:i] + s[i + 2:])
                    else:
                        return y + score(s[0:i + 1] + s[i + 3:])
                elif s[i: i + 2] == 'bab':
                    if x <= y:
                        return x + score(s[0:i] + s[i + 2:])
                    else:
                        return y + score(s[0:i + 1] + s[i + 3:])
            score1 = score2 = 0
            for i in range(0, len(s) - 1):
                if s[i: i + 2] == 'ab':
                    score1 = x + score(s[0:i] + s[i + 2:])
                break
            for i in range(0, len(s) - 1):
                if s[i: i + 2] == 'ba':
                    score2 = y + score(s[0:i] + s[i + 2:])
                break
            return max(0, score1, score2)

        return score(s)

if __name__ == '__main__':
    s = Solution()
    x = s.maximumGain('adbcab', 4, 5)
    print(x)