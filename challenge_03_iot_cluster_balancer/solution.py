from typing import List
import sys

def feasible(loads: List[int], k: int, M: int) -> bool:
    segments = 1
    curr = 0
    for x in loads:
        if x > M:
            return False
        if curr + x <= M:
            curr += x
        else:
            segments += 1
            curr = x
    return segments <= k

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    loads = [int(next(it)) for _ in range(n)]
    left = max(loads)
    right = sum(loads)
    while left < right:
        mid = (left + right) // 2
        if feasible(loads, k, mid):
            right = mid
        else:
            left = mid + 1
    print(left)

if __name__ == "__main__":
    solve()

