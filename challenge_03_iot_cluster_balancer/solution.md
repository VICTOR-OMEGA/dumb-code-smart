The minimal possible maximum segment sum lies between:

L = max(loads) (a segment must at least hold the largest single device), and

R = sum(loads) (everything on one server).

We binary-search M on [L, R] asking: can we partition into ≤ k segments such that every segment sum ≤ M? If yes, M is feasible; try smaller. If no, increase M.

Feasibility (check) is done greedily from left to right: accumulate device loads into current segment until adding next device would exceed M, then start a new segment. If total segments used ≤ k, M is feasible; otherwise not.

Why greedy works: for the contiguous partition problem with fixed M the greedy left-to-right packing minimizes number of segments used and any feasible packing can be transformed to the greedy packing without increasing segment sums or segment counts. So feasibility check is correct.


Algorithm

Read n, k, then loads[0..n-1].

left = max(loads), right = sum(loads).

While left < right:

mid = (left + right) // 2

If feasible(mid) → right = mid

Else → left = mid + 1

Print left (the minimal feasible maximum).

feasible(M):

segments = 1, curr = 0

For each x in loads:

If x > M: return False (single element exceeds M)

If curr + x <= M: curr += x

Else: segments += 1; curr = x

Return segments <= k

Correctness proof

Lower bound: any partition must have a segment containing the maximum element, so optimal answer ≥ max(loads).

Upper bound: putting all elements in one segment yields sum(loads).

Monotonicity: If M is feasible (we can partition with max ≤ M), then any M' ≥ M is also feasible. This monotonic predicate enables binary search.

Greedy check correctness: For a fixed M, greedy packs as much as possible in each segment; this minimizes the number of segments needed for that M. If greedy needs more than k segments, no other packing can use ≤ k while respecting contiguity and M. So feasibility result is sound.

Complexity

Feasibility check: O(n) (single pass)

Binary-search iterations: O(log S) where S = sum(loads) (upper bound magnitude). Practically log(sum) ≤ ~60 (since sum ≤ n·10⁹ and n ≤ 2e5).

Total time: O(n log S) (acceptable for n ≤ 2e5).

Space: O(1) extra (input space O(n)).

Implementation notes and pitfalls

Use 64-bit integers (Python int is arbitrary precision; in other languages use 64-bit) because sum(loads) may exceed 32-bit.

Avoid off-by-one in binary search: use while left < right with mid = (left + right) // 2 and move bounds as right = mid or left = mid + 1.

In feasible check, check if x > M: return False. it ensures we handle single huge elements early.

Be careful about exactly k segments requirement: the check allows ≤ k segments (we can always add empty segments conceptually to reach exactly k), but because segments must be non-empty, the greedy uses as few segments as possible; if it uses ≤ k, we can split some segments (if needed) to reach exactly k while not increasing the maximum. So segments <= k is the correct feasibility condition.

Edge cases

k == n → each device can be its own segment → answer = max(loads).

k == 1 → answer = sum(loads).

Single very large load among small loads → answer must at least be that large element.

Empty input: no output or define behavior.

