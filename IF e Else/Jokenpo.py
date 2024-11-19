print("Bem-Vido ao Jokenpo game!")
nome1 = str(input("Digite seu nome: "))
nome2 = str(input("Digite seu nome: "))

p1 = str(input(f"{nome1} Escolha entre pedra papel e tesoura: "))
p2 = str(input(f"{nome2}Escolha entre pedra papel e tesoura: "))

if (p1 == "pedra" and p2 == "tesoura") or (p1 == "papel" and p2 == "pedra") or (p1 == "tesoura" and p2 == "papel"):
    print(f"{nome1} Ganhou!")
elif (p1 == "tesoura" and p2 == "pedra") or (p1 == "pedra" and p2 == "papel") or (p1 == "papel" and p2 == "tesoura"):
    print(f"{nome2} Ganhou!")
elif (p1 == p2):
    print("Empate")
else:
    print("Erro")