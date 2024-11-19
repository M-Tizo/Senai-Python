#imprimir gol da alemanha 7 vezes
"""
gols = 0
while gols < 7:
    gols = gols + 1
    print("Gol da Alemanha")

gol = 0
while gol <1:
    gol = gol +1
    print("Gol do Brasil")
print(f"Placar \n Alemanha: {gols} \n Brasil: {gol}")
print(f" GER: {gols} x BRA: {gol}")

valor = 0
while valor <= 10:
    print(valor)
    valor = valor + 1

contador = 1
soma = 0
while contador <= 5:
     soma = soma + contador
     contador = contador + 1
print(f"A soma é {soma}")

#else

x = 0
while x < 10:
    print(f"O valor de x nesta iteração é {x}")
    print("X ainda é menor que 10, somando 1 a x")
    x = x + 1 
else:
    print("Acabou o loop")
print(x)

valor = int(input("Quanto é 2 + 2: "))
while valor != 22: 
    print("Erorouuuuuuuuuuuuuuuuu!")
    valor = int(input("Quanto é 2 + 2:"))
else:
    print("Certa a resposta!")

#pass, break
valor = 0
while valor <10:
    if valor == 4:
        continue# continua o codigo!
        #break #Para o codigo!
    else:
        pass #Instrução nula
         #nenhuma ação específica
    print(valor)
    valor = valor + 1 

#Média da sala de aula usando while
#Quando utilizar o While True tem que colocar o break.
notas = 0
qtd_notas = 0
while True:
    nota = float(input("Informe a nota (-1 para finalizar): "))
    if nota == -1:
        break
    notas += nota
    # notas = notas + 1
    qtd_notas = qtd_notas + 1

if qtd_notas > 0:
    print(f"Quantidade de notas informadas {qtd_notas}")
    print(f"Média das notas: {notas / qtd_notas:.2f}")
else:
    print("Nenhuma nota informada!")

teste = input("Digite sim: ").upper()
teste2 = input("Digite sim: ").lower()
teste3 = input("Digite sim: ").capitalize()
print(teste)
print(teste2)
print(teste3)

while True:
    python = input("Você gosta de Python? ").upper()
    if python == "SIM":
        print("Resposta correta")
        break
    elif python == "NÃO":
        print("Que pena!")
        break
    else:
        print("esta não é a resposta correta")


while True:
    nota = float(input("Digite sua nota: "))
    if nota >=7 and nota <= 10:
        print(f"Sua nota foi {nota:.2f} parabens você tirou uma boa nota e passou! ")
        break
    elif nota <= 6 and nota >= 5:
        print(f"sua nota foi {nota} você passou!")
        break
    elif nota <=4 and nota >=0:
        print(f"sua nota foi {nota} você está de recuperação!")
        break
    else:
        print("nota invalida!")

notas = 0
q_notas = 0
while True:
    nota = float(input("Digite sua nota (use -1 caso n tenha mais notas para digitar): "))
    if nota == -1:
        break
    q_notas = q_notas + 1
    notas += nota
if q_notas > 0:
    print(f"você tem {q_notas} notas")
    print(f"Sua média é de {notas/q_notas}")
else:
    print("Notas invalidas!")


alunos = 0 
turmas = 0
while True:
    t_alunos = int(input("Quantos alunos tem na sua turma? "))
    if t_alunos > 40:
        t_alunos = int(input("Quantia invalida digite uma correta: "))
    turmas = turmas + 1
    print(f"Tem {t_alunos} alunos na turma {turmas}")
    alunos += t_alunos
    end = input("Tem Mais alguma turma? (S/N)  ").upper()
    if end == "N":
        print(f"temos {turmas} turmas e um total de {alunos} alunos logo a média de alunos por turma é {alunos / turmas}")
    else:
        pass    
"""
