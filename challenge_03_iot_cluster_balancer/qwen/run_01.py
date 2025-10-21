import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); k = int(next(it))
    loads = [int(next(it)) for _ in range(n)]
    # naively split by count
    res = []
    base = n // k
    extra = n % k
    idx = 0
    for i in range(k):
        cnt = base + (1 if i < extra else 0)
        s = sum(loads[idx:idx+cnt]) if cnt>0 else 0
        res.append(s)
        idx += cnt
    print(max(res))

if __name__ == "__main__":
    main()

