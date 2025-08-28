try:
    preco = float(input("Preço unitário do produto: "))
    unidade = int(input("Quantidade comprada: "))
    dinheiro = float(input("Dinheiro recebido: "))

    Valor_total = preco * unidade

    if Valor_total < dinheiro:
        troco = dinheiro - Valor_total
        
        print(f"TROCO: R${troco:.2f}")
    else:
        troco = Valor_total - dinheiro

        print(f"DINHEIRO INSUFICIENTE. FALTAM R${troco:.2f}")

except ValueError:
    print("Entrada inválida. Utilize apenas números.")