class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictionary = {}
        for n in nums:
            if n in dictionary:
                continue
            dictionary[n] = [n, n]
            if n+1 in dictionary and n-1 in dictionary:
                low = dictionary[n-1][0]
                high = dictionary[n+1][1]
                dictionary[low][1] = high
                dictionary[high][0] = low
            elif n-1 in dictionary:
                dictionary[n] = [dictionary[n-1][0], dictionary[n][1]]
                dictionary[n-1] = [dictionary[n-1][0], dictionary[n][1]]
                low = dictionary[n-1][0]
                dictionary[low][1] = n
            elif n+1 in dictionary:
                dictionary[n] = [dictionary[n][0], dictionary[n+1][1]]
                dictionary[n+1] = [dictionary[n][0], dictionary[n+1][1]]
                high = dictionary[n+1][1]
                dictionary[high][0] = n
        ans = 0
        for n in nums:
            ans = max(ans, dictionary[n][1] - dictionary[n][0] + 1)
        return ans

            
