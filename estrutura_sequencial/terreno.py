largura = float(input("Digite a largura do trerreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor_quadrado = float(input("Digite o valor quadrado do terreno: R$ "))

area = largura * comprimento
valor_terreno = area * valor_quadrado

print(f"ÁREA: {area:.2f}")
print(f"PREÇO DO TERRENO: R$ {valor_terreno:.2f}")