'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return "false"
        n = len(str(x))
        old_x = x
        new_x = 0
        for i in range(n):
            n -= 1
            new_x += (x % 10) * 10 ** n
            x = x // 10
        if old_x == new_x:
            return "true"
        return "false"
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def romanToInt(self, s: str) -> int:
        x = 0
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s) - 1):
            if dict[s[i]] < dict[s[i+1]]:
                x -= dict[s[i]]
            else:
                x += dict[s[i]]
        x += dict[s[-1]]
        return x



