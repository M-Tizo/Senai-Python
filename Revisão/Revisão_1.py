qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))
total = 0
for aluno in range(qtd_alunos):
    nota = float(input(f"Digite a nota do {aluno+1}° aluno: ")) 
    total += nota
print(f"A media da turma é: {total/qtd_alunos}")

print("Bem-vindo ao nosso validador")

nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

while tamanho_nome < 3:
    print("O nome deve conter mais de 3 caracteres!")
    nome = input("Digite seu nome: ")
    tamanho_nome = len(nome)

idade = int(input("Informe sua idade: "))

while idade < 0 or idade > 150:
    print("Idade invalida!")
    idade = int(input("Informe sua idade: "))

salario = float(input("Informe seu salario: "))

while salario <= 0:
    print("Salario invalido")
    salario = float(input("Informe seu salário: "))

sexo = input("Informe seu sexo (M/F): ").upper()

while sexo not in ["M", "F"]:
    print("Sexo inválido!")
    sexo = input("Informe seu sexo (M/F): ").upper()

estado_civil = input("Informe seu estado civil (S - Solteiro, C - Casado, V - Viúvo, D - Divorciado): ").upper()

while estado_civil not in ["S", "C", "V", "D"]:
    print("Estado civil invalido!")
    estado_civil = input("Informe seu estado civil (S - Solteiro, C - Casado, V - Viúvo, D - Divorciado): ").upper()

print(f"Cadastro valido Nome: {nome}, Idade: {idade}, Salário: {salario}, Sexo: {sexo}, Estado Civil: {estado_civil}")

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