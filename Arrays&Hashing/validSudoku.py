class Solution:

    map = {}

    def utility(self,i,j,strr,board):
        i1= i
        j1 = j

        while(j1<len(board)):
            if board[i][j1]!='.':
                map[board[i][j1]] = map.get(board[i][j1],0)+1
            
            j1+=1

        while(i1<len(board)):
            if board[i1][j]!='.':
                map[board[i1][j]] = map.get(board[i1][j],0)+1
            
            i1+=1
            
        for i in range(3):
            for j in range(3):
                if(board[i][j]==)
    
    
    
    
    def isValidSudoku(self, board: list[list[str]]):
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.utility(i,j,board[i][j],board)
               






board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
sol = Solution()

sol.isValidSudoku(board)


