class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols  = len(grid),len(grid[0])
        queue = deque()

        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 0 :
                    queue.append((r,c))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue :
            row,col = queue.popleft()

            for dr,dc in directions :
                new_row = row + dr
                new_col = col + dc

                if (
                    new_row < 0
                    or new_row >= rows
                    or new_col < 0
                    or new_col >= cols
                    or grid[new_row][new_col] != 2147483647
                ):
                    continue
                
                grid[new_row][new_col] = grid[row][col] + 1

                queue.append((new_row,new_col))
        
        