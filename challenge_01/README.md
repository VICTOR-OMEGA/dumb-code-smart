# Challenge 01: Identical Character Set Pairs

---

## Problem Statement

Given a list of strings, count how many unique index pairs (i, j) exist such that:

- 0 ≤ i < j < len(strs)
- Both strings contain exactly the same set of characters
- Ignore:
  - Case ("Good" and "god" >> valid)
  - Order ("abc" and "cba" >> valid)
  - Frequency ("aabc" and "cbaa" >> valid)

---

## Example

### Input:
- ["Good", "god", "yarn", "back", "aabc", "cbaa"]

### Output:
- 2

---

## Explanation:
- Pair (0,1): "Good" and "god" >> {'g', 'o', 'd'}
- Pair (4,5): "aabc" and "cbaa" >> {'a', 'b', 'c'}

