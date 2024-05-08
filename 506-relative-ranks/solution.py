class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        positions = {}
        for i, s in enumerate(score):
            positions[s] = i

        sortedScores = sorted(score, reverse = True) 
        for i, s in enumerate(sortedScores):
            if i == 0:
                score[positions[s]] = "Gold Medal"
            elif i == 1:
                score[positions[s]] = "Silver Medal"
            elif i == 2:
                score[positions[s]] = "Bronze Medal"
            else:
                score[positions[s]] = str(i + 1)
        return score




