n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if (n1<n2 and n1<n3):
    print(f"Menor numero= {n1}")
elif (n2<n3):
    print(f"Menor numero= {n2}")
else:
    print(f"Menor numero= {n3}")

