


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


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
