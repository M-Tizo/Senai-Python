'''#Operadores de comparação
#Retorna sempre a um valor booleano
#maior que
print(6>3)
#Maior ou igual a 
print(6>=6)
#menor que
print(4<5)
#Menor ou igual
print(4<=5)
#igual a 
print(8==8)
#Diferente de
print(8!=9)

x=8
x1=3
print(x<x1)
print(x == x1)
print(x >= x1)
print(x != x)'''

"""
idade = int(input("digite sua idade: "))
if idade>= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")"""

"""if 5==5:
    print("Testando python")

if True:
    print("Você gosta de python")"""

'''media = float(input("digite a media do aluno: "))
if media > 7:
    print("Aprovado!")
elif media <5:
    print("Reprovado!")
else:
    print("Recuperação!")'''

"""if 5<2:
    print("Verdadeiro!")
else:
    print("É falso!")"""
'''while True:
    dia = str(input("Digite o dia de hoje em minusculo: "))
    if dia == "segunda":
        print("Hoje fará sol")
    elif dia == "terça":
        print("Vai chover!")
    elif dia == "quarta":
        print("Hoje fará sol!")
    elif dia== "quinta":
        print("Vai chover!")
    elif dia == "sexta":
        print("Vai nevar!")
    elif dia == "sábado":
        print("Vai estar frio!")
    elif dia == "domingo":
        print("Vai fazer sol!")
    else:
        print("Sem previsão de tempo para o dia selecionado!")
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
if n1>n2:
    print(f"{n1} é o maior numero e {n2} é o menor")
elif n1<n2:
    print(f"{n2} é o maior numero e {n1} é o menor")
else:
    print(f"{n2} é igual a {n1}")

num = int(input("Digite um numero: "))
result=num%2
if result== 0:
    print(f"{num} é um numero par")
else:
    print(f"{num} é um numero ímpar")'''

"""print("Bem vindo ao programa de estado civil")
print("Digite seu estado civil: \n C \n S \n D \n V \n O")
resposta=str(input("Resposta: "))
if resposta == "C" or resposta== "c":
    print("C-Casado")
elif resposta== "S" or resposta=="s":
    print("S-Solteiro")
elif resposta== "D" or resposta== "d":
    print("D-Divorciado")
elif resposta== "V" or resposta== "v":
    print("V-Viúvo")
elif resposta== "O" or resposta== "o":
    print("O-Outros")
else:
    print("estado civil não encontrado digite outro")"""

"""idade = 16
nome = "Gabriel"
if idade >= 18:
    if nome=="Gabriel":
        print("Bem-vindo , chefe! Sua mesa VIP está te esperando!")
    else:
        print("Seja bem-vindo")
else:
    if nome== "Gabriel":
        print("Bem-vindo, chefe! sua mesa VIP está te esperando!")
    else:
        print("Desculpe, você não pode entrar, precisa ter 18 anos!")"""
"""
nota = int(input("Digite suas notas: "))
faltas= int(input("Digite suas faltas: "))

if nota >= 70:
    if faltas<= 5:
        print("Aprovado!")
    else:
        print("Reprovado por falta!")
else:
    if faltas >5:
        print("Reprovado por faltas e por nota!")
    else:
        print("Reprovado por nota.")"""
# and depende de var verdadeiras, or depende de 1 verdadeira , not ele inverte o resultado do and 
#Operadores logicos
"""idade_lucas = 21
idade_Pedro = 19

if (idade_lucas >= 18) and idade_Pedro >= 18:
    print("as duas condições são verdadeiras logo eles tem mais de 18 anos")"""

"""idade_lucas = 21
idade_pedro = 19
if (idade_lucas >= 18) or (idade_pedro >= 18):
    print("Pelo menos uma das condições são verdadeiras")"""

"""idade_lucas = 16
idade_pedro = 19
if not(idade_lucas >=18):
    print("Invertir o valor")"""

"""print("Bem-vindo ao sistema de voto")
idade = int(input("Digite sua idade: "))
if (idade < 18 ) or (idade >= 70):
    if (idade < 16):
        print("não vota")
    else:
      print("Voto Facultativo")
elif (idade >=18):
    print("Voto obrigatorio")


print("Bem-vindo ao sistema de detecção de classificação")
idade = int(input("Digite sua idade: "))

if (idade >= 5) and (idade <=7):
    print("Infantil A")
elif (idade >= 8) and (idade <= 11):
    print("Infantil B")
elif (idade >= 12) and (idade <= 13):
    print("Juvenil A")
elif (idade >= 14) and (idade <= 17):
    print("Juvenil B")
elif (idade >= 18):
    print("Adultos")
else:
    print("Você não tem idade o suficiente")

num1= float(input("Digite um numero: "))
num2= float(input("Digite outro numero: "))

op= str(input("Escolha a operação: \n soma \n subtração \n multiplicação \n divisão \n : "))
if (op == "soma") or (op =="+"):
    print(f"{num1} + {num2} = {num1+num2}")
elif (op == "subtração") or (op=="-"):
    print(f"{num1} - {num2} = {num1-num2}")
elif (op == "multiplicação") or (op == "x") or (op=="*") or (op== "X"):
    print(f"{num1} X {num2} = {num1*num2}")
elif (op == "divisão") or (op == "/"):
    print(f"{num1} / {num2} = {num1/num2}")
else:
    print("favor utilizar apenas as opções dadas.")
"""
"""altura = float(input("Digite a altura em cm: "))
largura = float(input("digite a largura em cm: "))
comprimento= float(input("digite o comprimento em cm: "))
consumo_medio_diario = float(input("digite o consumo medio diario em litros: "))

metro_cubico = (altura*comprimento*largura) / 1000
autonomia= metro_cubico/consumo_medio_diario

print(f"a capacidade total do reservatorio em litros é {metro_cubico} L")
print(f"a autonomia do reservatorio é de {autonomia}")

if (autonomia < 2):
    print("consumo elevado")
elif (autonomia >= 2) and (autonomia <= 7):
    print("Consumo moderado")
elif (autonomia >7):
    print("Consumo reduzido")"""

"""print ("Bem-Vindo ao akinator dos numeros")
print("Pense em um numero e eu vou adivinhar!")
q1 = input("Seu numero é menor que 10? ")
if q1 == "sim":
    q2 = input("é menor que 5? ")
    if q2 == "sim":
        q4 = input("é maior que 2? ")
        if q4 == "não":
            print("Seu numero é 1")
        else:
            print("seu numero é 2? ")
    else:
        q5 = input("é maior que 7? ")
else:
    print("Deve ser um numero de 1 a 10")"""

"""print ("Bem-Vindo ao akinator dos numeros")
print("Pense em um numero e eu vou adivinhar!")
q1 = input("Seu numero é par? (s/n) ")
if q1 == "s":
    q2 = input("Seu numero é menor que 9? (s/n) ")
    if q2 == "s":
        q4 = input("Seu numero é maior que 7? (s/n) ")
        if q4 == "s":
            r2 = input("seu numero é 8? (s/n) ")
            if r2 == "s":
                print("Eu Ganhei!")
        else:
            q5 = input("seu numero é maior que 3?(s/n )")
            if q5 == "n":
                r3 = input("seu numero é 2? (s/n) ")
                if r3 == "s":
                    print("Eu Ganhei!")
            else: 
                q6 = input( "seu numero é maior que 5? (s/n) " )
                if q6 == "s":
                    r4 = input("Seu numero é 6? (s/n) ")
                    if r4 == "s":
                        print("Eu Ganhei!")
                else:
                    q7 = input("Seu numero é 4? (s/n) ")
                    if q7 == "s":
                        print("Eu Ganhei")        
    else: 
        r1 = input("Seu numero é 10? (s/n) ")    
        if r1 == "s":
            print("Eu ganhei")
else:
    q3 = input("seu numero é menor que 8? (s/n) ")
    if q3 == "s":
        q8 = input("seu numero é maior que 2? (s/n) ")
        if q8 == "s":
            q9 = input("seu numero é menor que 4? (s/n) ")
            if q9 == "s":
                r7 = input("Seu numero é 3? (s/n) ")
                if r7 == "s":
                    print("Eu ganahei")
            else:
                q10 = input("Seu numro é maior que 6? (s/n) ")
                if q10 == "s":
                    r8 = input("Seu numero é 7? (s/n) ")
                    if r8 == "s":
                        print("Eu Ganhei")
                else:
                    r9 = input("Seu numero é 5? (s/n) ")
                    if r9 == "s":
                        print("Eu Ganhei!")                
        else:
            r6 = input("Seu numero é 1? (s/n) ")
            if r6 == "s":
                print("Eu Ganhei")    
    else:
        r5 = input("Seu numero é 9? (s/n) ")
        if r5 == "s":
            print("Eu Ganhei")
            """
