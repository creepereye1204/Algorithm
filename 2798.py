from itertools import combinations
_, limit = map(int, input().split())
print(max([sum(nums) if sum(nums) <= limit else
      1 for nums in combinations(list(map(int, input().split())), 3)]))
