class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        part = ""
        arr = []
        itr = 0
        start = 0
        while itr < len(s):
            c = s[itr]
            if c in part:
                arr.append(part)
                ind = s.index(c, start, itr) +1
                start = ind
                itr = ind
                part = s[itr]
            else:
                part += c
            itr += 1

        arr.append(part)
        return max(len(x) for x in arr)


obj = Solution()
q = "bbbbbbbbb"
ans = obj.lengthOfLongestSubstring(q)
print(ans)