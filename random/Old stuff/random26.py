# return prefix, yadiyada. Heavily on strategy and understanding on various tools and common skills.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        self.strs = strs
        if not strs:
            return "lkj"

        for i, char in enumerate(strs[0]):
            print(i, char)
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
        return strs[0]


print(Solution().longestCommonPrefix(["flower", "flow", "floght"]))
