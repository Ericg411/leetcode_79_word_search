from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_exists = False
        def exists(r, c, word_index, used):
            nonlocal word_exists
            if word_index == len(word):
                word_exists = True
                return
            else:
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for (dr, dc) in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (nr, nc) not in used and board[nr][nc] == word[word_index]:
                        used.add((nr, nc))
                        exists(nr, nc, word_index + 1, used)
                        used.remove((nr, nc))




        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == word[0]:
                    used = set()
                    used.add((row, col))
                    exists(row, col, 1, used)
                    if word_exists:
                        return True
            
        return False