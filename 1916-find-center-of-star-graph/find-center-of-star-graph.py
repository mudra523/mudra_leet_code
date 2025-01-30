class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        centerGraph = {}

        for s, d in edges:
            centerGraph[s] = centerGraph.get(s, 0) + 1
            centerGraph[d] = centerGraph.get(d, 0) + 1

        for node, count in centerGraph.items():
            if count == len(edges):
                return node

        return -1
        