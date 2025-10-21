# iot_cluster_balancer

Partition an ordered sequence of device loads into exactly k contiguous segments (servers) to minimize the maximum server load.

Files:
- `solution.py` : optimal solution (binary search + greedy).
- `generator.py` : random test generator for local use.
- `problem.md`, `idea.md`, `solution.md` : docs.
- `requirements.json` : time/memory.
