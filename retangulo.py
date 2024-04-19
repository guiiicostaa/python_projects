import math

area: float; perimetro: float; diagonal: float

base= float(input("Digite o valor da base do retangulo: "))
altura= float(input("Digite o valor da altura do retangulo: "))

area =base*altura
perimetro = 2*(base+altura)
diagonal = math.sqrt((base**2) + (altura**2))

print(f"Area= {area:.4f}")
print(f"Perimetro= {perimetro:.4f}")
print(f"Diagonal= {diagonal:.4f}")

