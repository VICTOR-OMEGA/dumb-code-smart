import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); k = int(next(it))
    loads = [int(next(it)) for _ in range(n)]
    cap = sum(loads) // k
    segments = 1
    curr = 0
    max_seg = 0
    for x in loads:
        if curr + x <= cap:
            curr += x
        else:
            max_seg = max(max_seg, curr)
            segments += 1
            curr = x
    max_seg = max(max_seg, curr)
    print(max_seg)

if __name__ == "__main__":
    main()

