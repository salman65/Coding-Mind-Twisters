class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


obj = Solution()
q = 101
ans = obj.isPalindrome(q)
print(ans)