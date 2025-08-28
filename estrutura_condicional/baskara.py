import math

try:
    a = float(input("Coeficiente A: "))
    b = float(input("Coeficiente B: "))
    c = float(input("Coeficiente C: "))

    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        print("Está equação não possuí raízes reais.")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print(f"X1: {x1:.4f}")
        print(f"X2: {x2:.4f}")

except ValueError:
    print("Entrada inválida. Utilize apenas números.")