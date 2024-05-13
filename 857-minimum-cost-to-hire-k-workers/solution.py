import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # sort based on smallest

        wOq = [[wage[i]/quality[i], quality[i]] for i in range(len(quality))]

        wOq.sort(key=lambda x: x[0])

        answer = float("inf")
        total_quality = 0

        lowestQuality = []

        for i in range(len(quality)):
            heapq.heappush(lowestQuality, -wOq[i][1])
            total_quality += wOq[i][1]

            if len(lowestQuality) > k:
                total_quality += heapq.heappop(lowestQuality)
            if len(lowestQuality) == k:
                answer = min(answer, total_quality * wOq[i][0])
        return answer






        