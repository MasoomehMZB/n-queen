import tkinter as tk
from tkinter import ttk
from controller.controller import NQueenController

class NQueenGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("N-Queens Solver")

        self.controller = NQueenController(self)

        self.n_label = tk.Label(root, text="Board Size (N):")
        self.n_label.pack()

        self.n_entry = tk.Entry(root)
        self.n_entry.insert(0, "8")
        self.n_entry.pack()

        self.method = tk.StringVar(value="backtracking")
        self.method_menu = ttk.Combobox(root, textvariable=self.method, values=["backtracking", "genetic"])
        self.method_menu.pack()

        self.solve_btn = tk.Button(root, text="Solve", command=self.handle_solve)
        self.solve_btn.pack()

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.info_label = tk.Label(root, text="")
        self.info_label.pack()

    def handle_solve(self):
        self.canvas.delete("all")
        try:
            size = int(self.n_entry.get())
        except ValueError:
            self.show_info("Invalid input for N.")
            return

        method = self.method.get()
        self.controller.solve(size, method)

    def show_solution(self, positions, size):
        cell_size = 400 // size
        for row in range(size):
            for col in range(size):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                fill = "white" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill)
                if positions[row] == col:
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="red")

    def show_info(self, text):
        self.info_label.config(text=text)

    def animate_backtracking(self, path, size, delay=500):
        self.step_index = 0
        self.path = path
        self.board_size = size
        self.delay = delay
        self._animate_step()

    def _animate_step(self):
        if self.step_index >= len(self.path):
            return  # End of animation

        positions = self.path[self.step_index]
        self.show_solution(positions, self.board_size)
        self.step_index += 1
        self.root.after(self.delay, self._animate_step)

