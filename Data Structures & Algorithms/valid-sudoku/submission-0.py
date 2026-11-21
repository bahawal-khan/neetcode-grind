class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ##check for rows
        for row in board:
            numbers = [x for x in row if x!='.']
            if len(numbers) != len(set(numbers)):
                return False

       

        ## now check for columns
        for col in range(9):
            numbers = []
            for row in range(9):
                if board[row][col] !='.':
                    numbers.append(board[row][col])
            if len(numbers) != len(set(numbers)):
                return False
        
        ## now checks for 3*3 boxes
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                box = []
                for r in range(3):
                    for c in range(3):
                        box.append(board[box_row+r][box_col+c])
                numbers = [x for x in box if x!='.']
                if len(numbers)!= len(set(numbers)):
                    return False
        
            
        return True          
