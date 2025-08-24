segundo = int(input("Digite a duração em segundos: "))

hora = segundo // 3600
minuto = (segundo % 3600) // 60
resto = segundo % 60

print(f"{hora} : {minuto} : {resto}")