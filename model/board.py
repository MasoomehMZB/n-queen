class Board:
    def __init__(self, size, positions=None):
        # Initialize the board with given size and optional positions
        self.size = size
        self.positions = positions or [-1]*size

    def is_valid(self, row, col):
        # Check if placing a queen at (row, col) is valid
        for r in range(row):
            c = self.positions[r]
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def place_queen(self, row, col):
        # Place a queen at (row, col)
        self.positions[row] = col

    def __str__(self):
        # String representation of the board
        board = ''
        for r in range(self.size):
            for c in range(self.size):
                board += 'Q ' if self.positions[r] == c else '. '
            board += '\n'
        return board