conte: int
N = int(input("Digite a ordem da matriz: "))
mat: [[int]] = [[0 for x in range(N)] for x in range(N)]

for i in range(0,N):
    for j in range(0,N):
        mat [i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("Diagonal principal:")
for i in range(0,N):
    print(f"{mat[i][i]} ", end="")

print()
print("Quantidade de negativos")

conte= 0
for i in range(0,N):
    for j in range(0,N):
        if mat[i][j] < 0:
            conte= conte+1

print(conte)