# #ReviseWithArsh #6Companies30Days Challenge 2023

#Microsoft 

# 2) Combination Sum with a twist.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def try_combination(combination, n, start):
            if k == len(combination):
                if n == 0: result.append(combination.copy())
                return
            for i in range(start, 10):
                combination.append(i)
                try_combination(combination, n-i, i+1)
                combination.pop()
        try_combination([], n, 1)
        return result