class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows=len(grid)
        cols=len(grid[0])

        max_area=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area=self.dfs(grid,i,j,rows,cols)
                    max_area=max(area, max_area)
        return max_area
    
    def dfs(self,grid,i,j,rows,cols):
        if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0:
            return 0
        
        grid[i][j]=0
        area=1

        area+=self.dfs(grid,i+1,j,rows,cols)
        area+=self.dfs(grid,i-1,j,rows,cols)
        area+=self.dfs(grid,i,j+1,rows,cols)
        area+=self.dfs(grid,i,j-1,rows,cols)

        return area
    