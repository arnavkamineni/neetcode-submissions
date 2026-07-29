class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for val in row:
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        miniBoard = {}

        for x in range(9):
            seen = set()
            for y in range(9):
                val = board[y][x]

                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

                    box = (x // 3, y // 3)
                    if box not in miniBoard:
                        miniBoard[box] = set()

                    if val in miniBoard[box]:
                        return False

                    miniBoard[box].add(val)

        return True