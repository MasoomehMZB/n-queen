from controller.backtrack import solve_backtracking


result, path, nodes = solve_backtracking(7)

print('result= \n', result)
print('num of nodes\n', nodes)

for b in path:
    print(b)
