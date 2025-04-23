# A magic square is an N×N grid of numbers in which the entries in each row, column and
# main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for
# N=4, 5, 6, 7, 8

import numpy as np

def generate_magic_square(n):
    if n % 2 == 1:
        # Siamese method (odd n)
        magic = np.zeros((n, n), dtype=int)
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic[i, j] = num
            i_new, j_new = (i - 1) % n, (j + 1) % n
            if magic[i_new, j_new]:
                i += 1
            else:
                i, j = i_new, j_new
        return magic

    elif n % 4 == 0:
        # Doubly even order
        magic = np.arange(1, n*n+1).reshape(n, n)
        mask = np.ones((n, n), dtype=bool)

        for i in range(n):
            for j in range(n):
                if ((i % 4 == j % 4) or (i % 4 + j % 4 == 3)):
                    mask[i, j] = False
        magic[mask] = (n*n + 1) - magic[mask]
        return magic

    elif n % 2 == 0:
        # Singly even (like 6, 10, etc.)
        half = n // 2
        mini_square = generate_magic_square(half)
        magic = np.zeros((n, n), dtype=int)
        add = [0, 2, 3, 1]
        for i in range(2):
            for j in range(2):
                magic[i*half:(i+1)*half, j*half:(j+1)*half] = (
                    mini_square + add[i*2 + j] * (half * half)
                )
        # Swap columns between top-left and bottom-left
        k = half // 2
        for i in range(half):
            for j in range(k):
                if j == k // 2:
                    continue
                magic[i, j], magic[i + half, j] = magic[i + half, j], magic[i, j]

        for i in range(half):
            for j in range(n - k + 1, n):
                magic[i, j], magic[i + half, j] = magic[i + half, j], magic[i, j]

        # Center column swap
        magic[:, [k]] = magic[:, [k + half]]
        magic[:, [k + half]] = magic[:, [k]]
        return magic

# Generate magic squares for N = 4, 5, 6, 7, 8
n = int(input("Enter the value of N "))
print(f"\nMagic Square (N = {n}):")
square = generate_magic_square(n)
print(square)
print("Row/Col/Diag sum =", n * (n**2 + 1) // 2)





