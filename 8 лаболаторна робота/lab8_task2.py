import numpy as np
import random

M = int(input("Введіть M: "))
N = int(input("Введіть N: "))

A = np.zeros((M, N), dtype=int)
for i in range(M):
    for j in range(N):
        A[i][j] = random.randint(1, 30)
print("Масив A:")
print(A)

Q = max(M, N)
B = np.zeros((Q, Q), dtype=int)
step = 1  
for i in range(Q):
    for j in range(Q):
        if i < M and j < N:
            B[i][j] = A[i][j]
        else:
            B[i][j] = 3 ** step
            step += 1
print("Масив B:")
print(B)
