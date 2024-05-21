class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        global ans
        ans = 0
        
        def recur(index, current):
            global ans
            if index == len(nums):
                return
            ans+=(current ^ nums[index])
            recur(index+1, current ^ nums[index])

            recur(index+1, current)

        recur(0, 0)
        return ans
