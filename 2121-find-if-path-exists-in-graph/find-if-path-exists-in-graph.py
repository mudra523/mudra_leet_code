class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #1. DFS with Recursion
        # if source == destination:
        #     return True

        # graph = defaultdict(list)
        
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # seen = set()
        # seen.add(source)

        # def dfs(i):
        #     if i == destination:
        #         return True
            
        #     for nei_node in graph[i]:
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             if dfs(nei_node):
        #                 return True
        #     return False

        # return dfs(source)

        #2. DFS with Stack:
        if source == destination:
            return True

        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for i in graph[node]:
                if i not in seen:
                    seen.add(i)
                    stack.append(i)
        return False