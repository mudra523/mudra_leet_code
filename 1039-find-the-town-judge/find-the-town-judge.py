class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int) # incoming - outgoing = n - 1 - 0 = n -1
        for src, dst in trust:
            delta[src] -= 1
            delta[dst] += 1
        
        for i in range(1, n + 1):
            if delta[i] == n -1:
                return i
        return -1
        # Solution1 Hashmap TC = SC = O(N)
        # incoming = defaultdict(int)
        # outgoing = defaultdict(int)

        # for src, dst in trust:
        #     outgoing[src] += 1
        #     incoming[dst] += 1

        # for i in range(1, n + 1):
        #     if outgoing[i] == 0 and incoming[i] == n - 1:
        #         return i
        # return -1