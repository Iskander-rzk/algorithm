


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        prefix = ""
        n = len(strs)
        for i in range(len(strs[0])):
            for j in range(1, n):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

    def isValid(self, s: str) -> bool:
        l = []
        for i in range(len(s)):
            if s[i] in "({[":
                l.append(s[i])
            elif len(l) == 0:
                return False
            elif s[i] == ")" and l[-1] != "(":
                return False
            elif s[i] == "]" and l[-1] != "[":
                return False
            elif s[i] == "}" and l[-1] != "{":
                return False
            else:
                l.pop()
        if len(l) != 0:
            return False
        return True


s = Solution()
print(s.isValid("({}"))
