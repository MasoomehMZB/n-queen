from model.backtrack import solve_backtracking
from model.genetic_algorithm import solve_genetic

class NQueenController:
    def __init__(self, view):
        self.view = view  # reference to the GUI class

    def solve(self, size, method):
        # Dispatches the solving method based on user selection
        if method == "backtracking":
            result = solve_backtracking(size)
            if result:
                board, path, expanded = result
                self.view.show_solution(board.positions, size)
                self.view.animate_backtracking(path, size)
                self.view.show_info(f"Expanded Nodes: {expanded[0]}")
            else:
                self.view.show_info("No solution found.")
        elif method == "genetic":
            solution, generation_best = solve_genetic(size)
            self.view.show_solution(solution, size)
            self.view.show_info(f"Generations: {len(generation_best)}")
        else:
            self.view.show_info("Unknown method selected.")