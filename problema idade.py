media: float

print("Digite abaixo o nome e a idade de duas pessoas")
nome1 = str(input("Digite o nome da primeira pessoa: "))
idade1 = int(input("Digite a idade da primeira pessoa: "))
print()
nome2 = str(input("Digite o nome da segunda pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))
print()

media = (idade1+idade2)/2

print(f"A idade média entre {nome1} e {nome2} é de {media:.1f} anos!!")