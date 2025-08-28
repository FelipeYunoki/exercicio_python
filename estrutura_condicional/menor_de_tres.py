try:
    num_1 = int(input("Primeiro valor: "))
    num_2 = int(input("Segundo valor: "))
    num_3 = int(input("Terceiro valor: "))

    if num_1 < num_2 and num_1 < num_3:
        print(f"MENOR: {num_1}")
    elif num_2 < num_3:
        print(f"MENOR: {num_2}")
    else:
        print(f"MENOR: {num_3}")

except ValueError:
    print("Entrada inválida. Utilize apenas números.")