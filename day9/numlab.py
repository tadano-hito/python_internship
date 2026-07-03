from __future__ import annotations
from itertools import permutations
import numpy as np
import time


def to_cost_matrix(profit: np.ndarray) -> np.ndarray:
    cost = profit.max() - profit
    return cost

def solve_brute_force(profit: np.ndarray) -> tuple[list[int], int]:
    n=profit.shape[0]
    best_perm=None
    best_total=-1
    for perm in permutations(range(n)):
        total=sum(profit[i][perm[i]] for i in range(n))
        if total>best_total:
            best_total=total
            best_perm=perm
    return list(best_perm), best_total

def _try_augment(row, cost, n, assignment, visited_cols):
    for col in range(n):
        if cost[row][col] == 0 and not visited_cols[col]:
            visited_cols[col] = True
            if assignment[col] == -1 or _try_augment(assignment[col], cost, n, assignment, visited_cols):
                assignment[col] = row
                return True
    return False


def _find_assignment(cost, n):
    assignment = [-1] * n
    for row in range(n):
        _try_augment(row, cost, n, assignment, [False] * n)
    assigned_rows = [-1] * n
    for col in range(n):
        if assignment[col] != -1:
            assigned_rows[assignment[col]] = col
    return assigned_rows


def solve_hungarian(profit: np.ndarray) -> tuple[list[int], int]:
    cost = to_cost_matrix(profit).astype(float)
    cost = cost - cost.min(axis=1, keepdims=True)
    cost = cost - cost.min(axis=0, keepdims=True)
    n = cost.shape[0]
 
    for _ in range(n * n):
        assigned_rows = _find_assignment(cost, n)
 
        if -1 not in assigned_rows:
            break
 
        covered_rows, covered_cols = _min_line_cover(cost, n, assigned_rows)
 
        if len(covered_rows) + len(covered_cols) >= n:
            break
 
        uncovered_rows = [i for i in range(n) if i not in covered_rows]
        uncovered_cols = [j for j in range(n) if j not in covered_cols]
 
        d = cost[np.ix_(uncovered_rows, uncovered_cols)].min()
        cost[np.ix_(uncovered_rows, uncovered_cols)] -= d
        if covered_rows and covered_cols:
            cost[np.ix_(covered_rows, covered_cols)] += d
 
    assigned_rows = _find_assignment(cost, n)
    total_profit = sum(profit[i][assigned_rows[i]] for i in range(n))
    return assigned_rows, int(total_profit)

def _min_line_cover(cost, n, assigned_rows):
    marked_rows = set(i for i in range(n) if assigned_rows[i] == -1)
    marked_cols = set()
    changed = True
    while changed:
        changed = False
        for i in marked_rows:
            for j in range(n):
                if cost[i][j] == 0 and j not in marked_cols:
                    marked_cols.add(j)
                    changed = True
        for j in marked_cols:
            for i in range(n):
                if assigned_rows[i] == j and i not in marked_rows:
                    marked_rows.add(i)
                    changed = True
    covered_rows = [i for i in range(n) if i not in marked_rows]
    covered_cols = list(marked_cols)
    return covered_rows, covered_cols



def verify(trials: int = 1000, max_n: int = 7) -> None:
    for t in range(trials):
        print(f"Trial {t}")
        n = np.random.randint(2, max_n + 1) 
        P = np.random.randint(1, 100, size=(n, n))
        
        _, total_brute = solve_brute_force(P)
        _, total_hungarian = solve_hungarian(P)
        
        assert total_brute == total_hungarian, f"MISMATCH on n={n}: brute={total_brute}, hungarian={total_hungarian}"
    
    print(f"All {trials} trials passed!")


def complexity_experiment():
    print(f"{'n':<5} {'Brute Force':>15} {'Hungarian':>15}")
    for n in range(2, 10):
        P = np.random.randint(1, 100, size=(n, n))
        start_time = time.perf_counter()
        solve_brute_force(P)
        brute_time = time.perf_counter()- start_time
        start_time = time.perf_counter()
        solve_hungarian(P)
        hungarian_time = time.perf_counter()- start_time
        print(f"{n:<5} {brute_time:>15.6f}s {hungarian_time:>15.6f}s")


# def verify(trials: int = 3, max_n: int = 7) -> None:
#     for _ in range(trials):
#         n = np.random.randint(2, max_n + 1) 
#         P = np.random.randint(1, 100, size=(n, n))
        
#         _, total_brute = solve_brute_force(P)
#         _, total_hungarian = solve_hungarian(P)
        
#         assert total_brute == total_hungarian, f"MISMATCH on n={n}: brute={total_brute}, hungarian={total_hungarian}"
    
#     print(f"All {trials} trials passed!")

if __name__ == "__main__":
    P = np.array([
        [9, 11, 14],
        [6, 15, 13],
        [12, 13, 6],
    ])
    print(solve_brute_force(P))
    print(solve_hungarian(P))
    verify()
    complexity_experiment()