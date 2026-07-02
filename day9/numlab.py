from __future__ import annotations
from itertools import permutations
import numpy as np

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


def solve_hungarian(profit: np.ndarray) -> tuple[list[int], int]:
    cost=to_cost_matrix(profit).astype(float)
    cost = cost - cost.min(axis=1, keepdims=True)
    cost = cost - cost.min(axis=0, keepdims=True)
    n = cost.shape[0]
    while True:
        assigned_rows = [-1] * n
        used_cols = [False] * n
    
        for i in range(n):
            for j in range(n):
                if cost[i][j] == 0 and not used_cols[j]:
                    assigned_rows[i] = j
                    used_cols[j] = True
                    break
        if -1 not in assigned_rows:
            break
        uncovered_rows = [i for i in range(n) if assigned_rows[i] == -1]
        uncovered_cols = [j for j in range(n) if not used_cols[j]]