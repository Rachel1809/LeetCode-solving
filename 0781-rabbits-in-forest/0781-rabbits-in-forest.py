class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        x = Counter(answers)
        res = 0
        for i, j in x.items():
            tmp = i + 1
            #res += -(-j//tmp) * tmp
            res += ceil(j/tmp) * tmp
        return res