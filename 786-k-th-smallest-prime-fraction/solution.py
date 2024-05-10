class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # 1 * (2, 3)/30, 1 * (2, 5)/30, 2 * (3)/30, 15/30, 18/30, 20/30

        possible = []
        for first in range(len(arr)):
            for second in range(first+1, len(arr)):
                num1 = arr[first]
                num2 = arr[second]
                possible.append([num1/num2, num1, num2])
        possible.sort()
        return possible[k-1][1:]


        