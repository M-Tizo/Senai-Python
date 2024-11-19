print("Sistema do caixo on")
print("Utilize 0 caso não tenha algum valor a ser inserido")
total_com_desconto = 0
while True:
    preço = float(input("Informe o valor do produto: "))
    if preço > 0: 
        total_com_desconto += preço
    elif preço == 0 and total_com_desconto < 1000:
        print(f"O total a pagar é de {total_com_desconto} $")
        break
    elif preço == 0 and total_com_desconto >= 1000:
        desconto = total_com_desconto * 0.1 
        desconto = total_com_desconto - desconto
        total_com_desconto -= desconto
        print(f"O total a pagar com o desconto de 10% é de {desconto}")
        break