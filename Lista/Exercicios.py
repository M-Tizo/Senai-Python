#Um programa que lê o vetor de 5 numeros inteiros e mostre-os

quantidade = 0
num = []
while True:
    num_new = num.append(input("Digite um número (use o 0 para sair): "))
    if num == 0 or quantidade >= 4:
        break
    quantidade += 1
for i in num:
    print(i)

#Um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa
num = []
quantidade = 0
while True:
    numero = float(input("digite um número (digite 0 para sair): "))
    num.append(numero)
    if numero == 0 or quantidade >= 9:
        break
    quantidade += 1
for i in num:
    print(i)

#Um programa que leia 4 notas, nostre as notas e a média na tela

qtd = 0
notas = []
while True:
    nota = float(input("Digite sua nota: "))
    notas.append(nota)
    if qtd == 3:
        break
    qtd += 1
media = sum(notas) / len(notas)
print("Suas notas foram:")
print(notas, end = "")
print(f"E a média das notas é: {media}")

#um programa que leio um vetor de 10 caracteres, e diz quantas consoantes foram lidas. impimindo elas

vogais = ["a", "e", "i", "o", "u"]
palavra = input("Digite uma palavra:").lower()
while len(palavra) >10:
    print("A palavra não pode ter mais de 10 caracteres")
    palavra = input("Digite uma palavra:").lower()
for letra in list(palavra):
    if letra in vogais:
        print(f"A letra {letra} é uma vogal")
    else:
        print(f"A letra {letra} é uma consoante")