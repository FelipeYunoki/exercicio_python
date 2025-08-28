try:
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))

    media = nota_1 + nota_2

    if media < 60:
        print(f"Nota final: {media}")
        print("REPROVADO")
    else: 
        print(f"Nota final: {media}")
        print("APROVADO")
except ValueError:
    print("Entrada inválida. Utilize apenas números.")