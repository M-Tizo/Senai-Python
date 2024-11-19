"""print("Bem-Vindo a tabuada automatica atualizada 2024 2.0")

numero = int(input("Digite um numero para a tabuada: "))
for i in range (1,11):
    print(f"{numero} X {i} = {numero*i}")"""

"""pessoas = int(input("Quantas pessoas são: "))
masculino = 0
outro = 0
for i in range (pessoas):
    genero = input("Sistema cadastral por favor informe seu sexo(F/M): ")
    if genero == "M" or genero == "m":
        masculino += 1
    else: 
        outro += 1
print(f"temos um total de {masculino} pessoas com o sexo masculino e {outro} pessoas com o gênero feminino ")"""

"""print("Programa que revela todos numeros pares")
quantia = int(input("Informe o numero: "))
for i in range (quantia):
    i%2
    if i%2 ==0:
        print(i)"""

"""soma = 0
for i in range (5):
    num = int(input("informe o numero: "))
    soma += num
print(f"a soma dos numeros é {soma} e a média é {soma/5}")        """

"""total = 0
pessoas = int(input("Quantas pessoas tem na sua turma: "))
for i in range (pessoas):
    idade = int(input(f"Quantos anos a pessoa {i+1} tem: "))
    total += idade
media = total / pessoas
if media <= 25 and media >= 0:
    print("A turma é jovem")
elif media >= 26 and media <= 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")"""

"""print("Bem vindo a Urna digital vamos descobrir o numero de votos de cada candidato")
print(" Renato Cariani = 1 \n Roberto Carlos = 2 \n Rogério Sene = 3")

cariani = 0
roberto = 0
sene = 0
nulo = 0

eleitores = int(input("quantos eleitores tem: "))
for i in range (eleitores):
    voto = int(input(f"Qual candidato o eleitor {i+1} votou: "))
    if voto == 1:
        cariani += 1
    elif voto == 2:
        roberto += 1
    elif voto == 3:
        sene += 1
    else:
        nulo += 1

if cariani > roberto and roberto > sene:
    print(f"A seguir o numero de votos de cada candidato: \n Renato Cariani = {cariani} \n Roberto Carlos = {roberto} \n Rogério Sene = {sene} \n Votos nulos = {nulo}")
elif roberto > cariani and cariani > sene:
    print(f"A seguir o numero de votos de cada candidato: \n Roberto Carlos = {roberto} \n Renato Cariani = {cariani} \n Rogério Sene = {sene} \n Votos nulos = {nulo}")
elif sene > roberto and roberto > cariani:
    print(f"A seguir o numero de votos de cada candidato: \n Rogério Sene = {sene} \n Roberto Carlos = {roberto} \n Renato Cariani = {cariani} \n Votos nulos = {nulo}")
elif sene > cariani and cariani > roberto:
    print(f"A seguir o numero de votos de cada candidato: \n Rogério Sene = {sene} \n Renato Cariani = {cariani} \n Roberto Carlos = {roberto} \n Votos nulos = {nulo}")
elif roberto > sene and roberto > cariani:
    print(f"A seguir o numero de votos de cada candidato: \n Roberto Carlos = {roberto} \n Rogerio Sene = {sene} \n Renato Cariani = {cariani} \n Votos nulos = {nulo}")
elif cariani > sene and sene > roberto:
    print(f"A seguir o numero de votos de cada candidato: \n Renato Cariani = {cariani} \n Rogerio Sene = {sene} \n Roberto Carlos = {roberto} \n Votos nulos = {nulo}")
else: 
    print(f"A seguir o numero de votos de cada candidato: \n Renato Cariani = {cariani} \n Rogerio Sene = {sene} \n Roberto Carlos = {roberto} \n Votos nulos = {nulo}")"""
