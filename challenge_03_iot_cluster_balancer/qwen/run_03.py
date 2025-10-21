import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); k = int(next(it))
    loads = [int(next(it)) for _ in range(n)]
    loads.sort(reverse=True)
    heap = [0]*k
    heapq.heapify(heap)
    for x in loads:
        smallest = heapq.heappop(heap)
        heapq.heappush(heap, smallest + x)
    print(max(heap))

if __name__ == "__main__":
    main()

