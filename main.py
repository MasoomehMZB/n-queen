from controller.genetic_algorithem import *

size = 12
res, list = solve_genetic(size)
print(res)

def p(res, size):
    board = ''
    for r in range(size):
        for c in range(size):
            board += 'Q ' if res[r] == c else '. '
        board += '\n'
    return board

print(p(res, size))
print(len(list))