from typing import List

def solution(strs: List[str]) -> int:
 seen = {}
    
 for s in strs:
  """Convert to lowercase and extract the unique character set"""
  key = frozenset(s.lower())
  if key in seen:
   seen[key] += 1
  else:
   seen[key] = 1

 #For each character set with more than one string, count combinations: nC2
 return sum(count * (count - 1) // 2 for count in seen.values() if count > 1)
