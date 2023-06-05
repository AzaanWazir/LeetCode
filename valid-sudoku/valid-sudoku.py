class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        columns = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        boxes = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        
        def getBox(i, j):
            x = i // 3
            y = j // 3
            return y * 3 + x
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                boxNum = getBox(i, j)
                
                if num in columns[i]:
                    print("BOOM")
                    return False
                if num in rows[j]:
                    print("BONG")
                    return False
                if num in boxes[boxNum]:
                    print("BING")
                    return False
                columns[i].add(num)
                rows[j].add(num)
                boxes[boxNum].add(num)
        return True
        