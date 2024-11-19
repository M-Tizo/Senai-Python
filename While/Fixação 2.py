print("Bem-vindo ao sistema de soma de numeros inteiros!")
soma = 0
while True:
    numero = int(input("Digite um numero inteiro (utilize 0 para ver o resultado): "))
    if numero == 0:
        break
    else:
        pass
    soma += numero
print(f"A soma dos numeros é {soma}") 