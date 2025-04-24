class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        t, f = 0, 0
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    f += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q and f > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= n or nj < 0 or nj >= m or grid[ni][nj] != 1:
                        continue
                    grid[ni][nj] = 2
                    q.append((ni, nj))
                    f -= 1
            t += 1

        return t if f == 0 else -1
