from typing import List

def is_prime_sieve(limit: int) -> List[bool]:
 sieve = [True] * (limit + 1)
 sieve[0:2] = [False, False]
 for i in range(2, int(limit**0.5) + 1):
  if sieve[i]:
   for j in range(i * i, limit + 1, i):
    sieve[j] = False
 return sieve

def special_pairs(n: int) -> List[List[int]]:
 primes = is_prime_sieve(n)
 res = []

 for a in range(2, n // 2 + 1):
  b = n - a
  if a < b and primes[a] and primes[b]:
   res.append([a, b])

 return res
