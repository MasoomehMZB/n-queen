import tkinter as tk

class NQueenGUI:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("N-Queen Solver")

        self.n_entry = tk.Entry(self.root)
        self.n_entry.insert(0, "8")
        self.n_entry.pack()

        self.method = tk.StringVar(value="backtracking")
        tk.Radiobutton(self.root, text="Backtracking", variable=self.method, value="backtracking").pack()
        tk.Radiobutton(self.root, text="Genetic Algorithm", variable=self.method, value="genetic").pack()

        tk.Button(self.root, text="Solve", command=self.solve).pack()

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

    def solve(self):
        n = int(self.n_entry.get())
        method = self.method.get()
        positions = self.controller.solve_nqueen(n, method)
        self.draw_board(n, positions)

    def draw_board(self, size, positions):
        self.canvas.delete("all")
        square_size = 400 // size
        for i in range(size):
            for j in range(size):
                x0 = j * square_size
                y0 = i * square_size
                x1 = x0 + square_size
                y1 = y0 + square_size
                fill = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
                if positions[i] == j:
                    self.canvas.create_oval(x0+5, y0+5, x1-5, y1-5, fill="red")
