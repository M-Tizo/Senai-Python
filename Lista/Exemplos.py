"""#Criando uma lista
bancos = ["Banco do Brasil", "Caixa", "Satander"]

#Criando uma lista vazia
meu_vetor = []

print(type(bancos))
print(bancos)

#Alterando um valor da lista
bancos[1] = "Inter"

#Alterando o ultimo elemento da lista
bancos[-1] = "C6"

print(bancos)

#percorrendo os valores do vetor
print(bancos[1])
for banco in bancos:
   print(banco)

bancos += ["Bradesco", "Nubank"]
print(bancos)


#Percorrendo os valores com for
cores = ["Vermelho", "Azul", "Verde", "Amarelo"]
for i in range(len(cores)): #4
    cor = cores[i]
    print(f"Cor no índice {i} é: {cor}")

#Criando uma lista de frutas
frutas = ["maçã", "banana", "laranja", "manga"]
print(f"Lista original: {frutas}")

#Adicionar uma fruta no final da lista/vetor
frutas.append("uva")
print(f"Lista após a adição de uva: {frutas}")

#inserindo uma fruta em uma posição
frutas.insert(2, "morango")
print(f"Lista após a inserção de morango: {frutas}")

#Remover uma fruta pelo nome
frutas.remove("laranja")
print(f"Lista após a remoção de laranja> {frutas}")

#Ordenando as frutas em ordem alfabética
frutas.sort()
print(f"Lista ordenada em ordem alfabética {frutas}")

#Invertendo a ordem da lista
frutas.reverse()
print(f"Lista invertida: {frutas}")

#Contar quantas vezes aparece uma fruta
qtd = frutas.count("manga")
print(f"A fruta manga aparece: {qtd} vezes")

#removendo a última fruta da lista e armazenando em uma variável
ultima_fruta = frutas.pop()
print(f"A última fruta removida foi: {ultima_fruta}")

#removendo frutas dentro de um intervalo de indices
del frutas[0:2]
print(f"Lista após a remoção de maçã e banana: {frutas}")

#Limpando todos os itens da lista
frutas.clear()
print(f"Lista após a limpeza: {frutas}")

#adicionar outros elementos de outra lista
frutas = ["maçã", "banana", "laranja", "manga"]
frutas_adicionais = ["uva", "morango"]
frutas.extend(frutas_adicionais)
print(f"Lista após a adição de outras frutas: {frutas}")

#usando index para encontrar a posição de um items
indice = frutas.index("laranja")
print(f"A fruta laranja está na posição: {indice}")

compras = [10,5,3,50,28,5] , ["tomate", "sabonete", "arroz", "feijão", "leite"]
print(compras)
produtos = compras[3]
print(produtos)
#Somando os valores
total = compras[0] + compras[1] + compras[2]
print(total)

#Adicionar elementos na lista fornecio pelo usuario
tarefas = []

tarefa = input("Digite uma tarefa: ")
tarefas.append(tarefa)
print(tarefas)

while tarefa != "":
    tarefa = input("Digite uma tarefa:")
    tarefas.appebd(tarefa)
print(tarefas)

#para verificar a existencia de um item na lista
Letras = ["a", "b", "c", "d", "e"]
var = input("Informe uma letra: ").lower()
if var in Letras:
    print(f"A letra {var} está na lista")
else:
    print(f"A letra {var} não está na lista")

nova = []
while True:
    num = int(input("digite um número inteiro (0 para sair): "))
    if num == 0:
        break
    nova.append(num)
print(nova)
#Somar itens da lista
print(sum(nova))
#maior valor da lista max()
print(max(nova))
#menor valor da lista min()
print(min(nova))

produtos = ["apple tv", "Air pods", "mac", "iphone 15", "ipad"]

novo_produto = produtos.append(input("Digite um novo produto: "))

#removendo um item
item_removido = input("Digite o produto que deseja remover: ").lower()

if item_removido in produtos:
    produtos.remove(item_removido)
    print(f"O produto {item_removido} foi removido da lista")
else:
    print(f"O produto {item_removido} não está na lista de produtos da apple ")
for i in produtos:
    print(i) or print(i, end = " - ")"""

"""
#Matriz

matriz = [
[1,2,3],
[4,5,6],
[7,8,9]
]

#matriz = [[1,2,3], [4,5,6], [7,8,9,]]

print(len(matriz))
print(matriz[0][1]) #elemento da primeira linha na segunda coluna: 2
print(matriz[1][2])#Elemento da segunda linha na terceira coluna: 6
"""

"""#percorrendo uma matriz

matriz = [[1,2,3],[4,5,6],[7,8,9]]

print("Elementos da matriz:")
print(f"Tamanho da minha matriz: {len(matriz)}")
for i in range (len(matriz)): 
    for j in range (len(matriz[i])):
        print(f"Elemento {i} {j} = {matriz[i][j]}")"""

#Criar uma matriz 3x3 com valores fornecidos pelo usuário
matriz = []

print("Prencha uma matriz 3x3")
for i in range (3):
    linha = []
    for j in range (3):
        valor = int(input(f"DIgite o valor para posição [{i}] [{j}] "))
        linha.append(valor)
        matriz.append(linha)
print("Matriz: ")
for linha in matriz:
    print(linha)