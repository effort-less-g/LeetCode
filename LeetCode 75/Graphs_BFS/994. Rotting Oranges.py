class Solution:


    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 2:
                    queue.append((i, j))
                
        size_i = len(grid)
        size_j = len(grid[0])
        res = 0
        changed = False
        visited = set()

        while queue:
            
            if changed:
                res += 1
            print(queue)

            changed = False
            # loc = queue[0]
            # if loc in visited:
            #     queue.pop(0)
            #     continue
            # queue.pop(0)
            # visited.add(loc)


            for locc in queue[:]:
                i = locc[0]
                j = locc[1]

                if i+1 < size_i and grid[i+1][j] == 1:
                    grid[i+1][j] =  2
                    queue.append((i+1, j))
                    changed = True
                if j+1 < size_j and grid[i][j+1] == 1:
                    grid[i][j+1] =  2
                    queue.append((i, j+1))
                    changed = True
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] =  2
                    queue.append((i-1, j))
                    changed = True
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] =  2
                    queue.append((i, j-1))
                    changed = True

                queue.pop(0)
            


        for row in grid:
            for col in row:
                if col == 1:
                    return -1
        
        return res
