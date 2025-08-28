try:
    glicose = float(input("Degite a medida da glicose: "))

    if glicose <= 100:
        print("Classificação: Normal")
    elif glicose <= 140:
        print("Classificação: Elevado")
    else:
        print("Classificação:Diabete")
except ValueError:
    print("Entrada inválida. Utilize apenas números.")