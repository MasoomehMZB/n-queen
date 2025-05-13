import tkinter as tk
from view.gui import NQueenGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = NQueenGUI(root)
    root.mainloop()