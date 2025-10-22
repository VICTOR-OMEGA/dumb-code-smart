Idea: IoT Cluster Balancer

Motivation
- In many IoT deployments (street sensors, pipeline sensors), devices are arranged along a physical line.
- Each server/gateway is responsible for a contiguous stretch of devices (range of sensors).
- We want to distribute devices to k servers such that the **maximum total load handled by any server** is minimized.

Why contiguous?
- Realistic for networks with geographically-ordered devices and gateway coverage.
- Makes the combinatorial problem solvable with binary search + greedy.

Rejected variants
- Arbitrary assignment to servers (NP-hard partition).
- Allow splitting device loads across servers (unrealistic).
- Minimize max-min difference directly as it is harder to decide; minimizing max load is standard and competitive.

Final choice
- Problem: Given n devices in fixed order and their integer loads, partition into k contiguous groups minimizing the maximum group sum.
- This gives a clear, optimal binary-search/check solution.

