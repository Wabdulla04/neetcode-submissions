class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subboxes = defaultdict(set)

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue
                if num in rows[i] or num in cols[j] or num in subboxes[(i // 3, j // 3)]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                subboxes[(i // 3, j // 3)].add(num)
        return True