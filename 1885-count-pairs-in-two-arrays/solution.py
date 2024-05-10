class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        nums = [nums1[i] - nums2[i] for i in range(len(nums1))]
        nums.sort()
        ans = 0
        for i in range(len(nums)-1):
            number = -nums[i] + 1
            left = i+1
            right = len(nums)-1
            while left<right:
                middle = (left + right)//2
                if nums[middle] >= number:
                    right = middle
                else:
                    left = middle+1
            if nums[i] + nums[left] > 0:
                ans += (len(nums)-1) - (left) + 1
        return ans

