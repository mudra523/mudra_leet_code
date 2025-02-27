class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            r, c, path_len = queue.popleft()

            if r == n-1 and c == n-1:
                return path_len

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, path_len + 1))
                    grid[nr][nc] = 1

        return -1