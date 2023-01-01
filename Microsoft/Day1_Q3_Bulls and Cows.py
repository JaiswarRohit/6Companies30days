# #ReviseWithArsh #6Companies30Days Challenge 2023

#Microsoft 

# 3) Bulls and Cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        bucket = [0] * 10
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                bucket[int(s)] += 1
                bucket[int(g)] -= 1
        return f'{bulls}A{len(secret) - bulls - sum(x for x in bucket if x > 0)}B'