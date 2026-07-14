class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0

        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 2 :
                    queue.append((r,c))
                elif grid[r][c] == 1 :
                    fresh += 1
        
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        while queue and fresh > 0 :
            for _ in range(len(queue)) :
                row,col = queue.popleft()
                for dr,dc in directions :
                    new_row = row + dr
                    new_col = col + dc

                    if (
                        new_row < 0 or
                        new_row >= rows or
                        new_col < 0 or
                        new_col >= cols
                    ) :
                        continue
                    if grid[new_row][new_col] != 1 :
                        continue
                    grid[new_row][new_col] = 2
                    fresh -= 1

                    queue.append((new_row,new_col))
            minutes += 1
        if fresh == 0 :
            return minutes
        return -1
        