"""
for i in range(7):
    print("Gol da alemanha")
for i in range(1):
    print("Gol do brasil")
    """
    #range tem 3 valores inicio,fim,salto sendo inicio de onde ele começa fim onde termina e salto de quanto em qaunto ele anda caso tenha só 1 digito ele será o fim e iniciara do 0 pulando de 1 em 1
# ele nunca roda o ultimo numero
"""
for i in range(10,20,2):
     print(i) 

for i in range(3):
     print(i)
"""   

#imprimir os valores no intervalo de 0 a 11:
"""
for contador in range(0,11,2):
     print(contador)

notas_alunos = [10,9,8,9,3]
for i in notas_alunos:
     print(i)
     if i == "foda":
          continue 
"""
#for (para cada) i (item) in (dentro) lista
"""
nome = "Gabriel"
for i in nome:
    print(i)
"""
#usando break para parar o for
"""
for gol in range(7):
    print("Gol da Alemanha")
    if gol == 6:
        break
print("Chega de gol")
print("Gol do Brasil")
"""
#usando o comando continue e else:
"""
for i in [1,10,20,30,35,40,50]:
    if i == 35:
#para pular o numero ou algo assim como pulou o 35
        continue
    print(i)
else:
    print("Acabou")
"""
#Somando os valores limitado a 50
"""
inicio = int(input("Digite o primeiro numero: "))
fim = int(input("Digite o Ultimo numero: "))
salto = int(input("Digite o salto: "))
total = 0
texto = "Calculo: "

for numero in range(inicio,fim,salto):
    total += numero
    texto += str(numero)
    if numero >= 50:
        break
    if numero != fim -1:
        texto = texto + " + "
print(texto)
print(total)
"""

#media de sala
"""
qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))
total = 0
for aluno in range(qtd_alunos):
    nota = float(input(f"Digite a nota do {aluno+1}° aluno: ")) 
    total += nota
print(f"A media da turma é: {total/qtd_alunos}")
"""