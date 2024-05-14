class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestSubstring(start, end):
            while 0<= start < len(s) and 0<= end < len(s):
                if s[start] != s[end]:
                    break
                start-=1
                end+=1
            return [max(0, end-start-2+1), s[start+1:end]]
        
        ans = s[0]
        for i in range(len(s)-1):
            same, ss = longestSubstring(i, i)
            diff, sd = longestSubstring(i, i+1)

            if len(ans) < same:
                ans = ss
            if len(ans) < diff:
                ans = sd

        return ans

