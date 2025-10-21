import random
import sys

def gen(n, k, maxv=100):
    loads = [random.randint(1, maxv) for _ in range(n)]
    s = "{} {}\n{}\n".format(n, k, " ".join(map(str, loads)))
    return s

if __name__ == "__main__":
    # print 5 sample cases
    for _ in range(5):
        print(gen(random.randint(1,10), random.randint(1,5), maxv=50))

