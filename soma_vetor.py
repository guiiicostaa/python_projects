N: int; x: int; soma: int
media: float

N = int(input("Quantos numeros ira digitar? "))
vet: [int]= [0 for x in range(N)]

soma = 0
for i in range (0,N):
    vet[i]= int(input("Digite um numero: "))
    soma = soma + vet[i]

media = soma/N

print()

print("Vetor: ", end="")
for i in range(0,N):
    print(f"{vet[i]} ", end="")
print()
print(f"Soma do vetor= {soma}")
print(f"Media= {media:.2f}")