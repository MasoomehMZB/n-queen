from model.board import Board

def solve_backtracking(size):
    board = Board(size)
    path = []
    expanded_nodes = [0]

    def backtrack(row):
        if row == size:
            return board, path.copy(), expanded_nodes

        for col in range(size):
            expanded_nodes[0] += 1
            if board.is_valid(row, col):
                board.place_queen(row, col)
                path.append(board.positions[:])
                result = backtrack(row + 1)
                if result:
                    return result
                path.pop()
                board.place_queen(row, -1)
        return None

    return backtrack(0)


