IoT Cluster Balancer
 Problem Statement

You are given `n` IoT devices arranged in a fixed order (e.g., along a street).
Each device `i` produces `loads[i]` kilobytes of data per second (positive integer).
You have `k` servers. Each server must handle a contiguous block of devices (non-overlapping).
Every device must be assigned to exactly one server.

Goal: Partition the sequence into exactly `k` contiguous segments such that the **maximum total load** handled by any server is minimized.

Input
- First line: two integers `n k` (1 ≤ k ≤ n ≤ 200000)
- Second line: `n` integers `loads[i]` (1 ≤ loads[i] ≤ 10^9)

Output
- Single integer: the minimal possible maximum server load (i.e., minimum over partitions of the maximum segment sum).

Examples

Example 1
Input:
5 3
10 20 15 5 25

Output:
25

Explanation:
Partition as [10,15] [20,5] [25] or [25] [20,5] [15,10] etc. Max load = 25.

Example 2
Input:
4 2
7 2 5 10

Output:
14

Explanation:
Partition as [7,2,5] [10] → segment sums 14 and 10 → max 14.

Notes
- Exactly k segments: some segments may have a single device.
- Time and memory constraints are in requirements.json.


