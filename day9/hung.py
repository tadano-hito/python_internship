import copy

def row_reduction(matrix):
    new_matrix = copy.deepcopy(matrix)
    for i in range(len(new_matrix)):
        row_min = min(new_matrix[i])
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] -= row_min
    return new_matrix

def column_reduction(matrix):
    new_matrix = copy.deepcopy(matrix)
    cols = len(new_matrix[0])
    for j in range(cols):
        col_min = min(new_matrix[i][j] for i in range(len(new_matrix)))
        for i in range(len(new_matrix)):
            new_matrix[i][j] -= col_min
    return new_matrix

def convert_to_minimization(matrix):
    flat_max = max(max(row) for row in matrix)
    new_matrix = copy.deepcopy(matrix)
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = flat_max - new_matrix[i][j]
    return new_matrix

def find_zero_assignment(matrix):
    n = len(matrix)
    assigned_rows = [-1] * n
    used_cols = [False] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0 and not used_cols[j]:
                assigned_rows[i] = j
                used_cols[j] = True
                break

    return assigned_rows

def print_matrix(matrix, title):
    print(f"\n{title}")
    for row in matrix:
        print(row)

def solve_assignment(cost_matrix, maximize=False):
    matrix = cost_matrix
    if maximize:
        matrix = convert_to_minimization(matrix)
        print_matrix(matrix, "Converted to Minimization")

    reduced = row_reduction(matrix)
    print_matrix(reduced, "After Row Reduction")

    reduced = column_reduction(reduced)
    print_matrix(reduced, "After Column Reduction")

    assignment = find_zero_assignment(reduced)

    print("\nFinal Assignment:")
    total = 0
    for worker, task in enumerate(assignment):
        if task != -1:
            value = cost_matrix[worker][task]
            total += value
            print(f"Worker {worker} -> Task {task} (value = {value})")

    label = "Total Profit" if maximize else "Total Cost"
    print(f"\n{label}: {total}")
    return assignment, total


if __name__ == "__main__":
    cost_matrix = [
        [2, 25, 18],
        [9, 4, 17],
        [11, 26, 1]
    ]

    print("=== MINIMIZATION ===")
    solve_assignment(cost_matrix, maximize=False)

    profit_matrix = [
        [62, 78, 50, 14],
        [71, 84, 61, 73],
        [87, 92, 111, 71],
        [48, 64, 87, 77]
    ]

    print("\n\n=== MAXIMIZATION ===")
    solve_assignment(profit_matrix, maximize=True)
