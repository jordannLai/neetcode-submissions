class Solution:
    def scoreOfString(self, s: str) -> int:
        # c o d e
        #     i
        #       j
        i = 0
        for x in range(len(s) - 1):
            i += abs(ord(s[x]) - ord(s[x+1]))
        return i