class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        positions = {}
        ans = 0
        start = 0
        for end in range(len(s)):
            char = s[end]
            if char in positions and positions[char] >= start:
                start = positions[char]+1
            positions[char] = end
            ans = max(ans, end-start+1)
        return ans


