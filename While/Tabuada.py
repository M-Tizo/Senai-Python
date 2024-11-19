print("Bem vindo ao sistema de tabuada")
acertos = 0
erros = 0
numero = 1

numero_t = int(input("Digite o numero que deseja treinar a tabuada: "))
while True:
    pergunta = int(input(f"quanto é {numero_t} X {numero}: "))
    
    calculo = numero * numero_t
    numero = numero + 1
    if pergunta != calculo:
     print(f"Resposta errada, a correta é {calculo}")
    else:
       print("Resposta correta!")
    if pergunta == calculo:
       acertos = acertos + 1
    else:
       erros = erros + 1
    if numero == 11:
       print(f"você teve {acertos} acertos e {erros} erros")
       pergunta2 = input("Quer jogar denovo? (S/N) ").upper()
       numero = 1
       acertos = 0
       erros = 0
       if pergunta2 == "N":
          print("Te vejo no proximo treino")
          break
       elif pergunta2 == "S":
         pergunta3 = input("Quer ir para proxima tabuada ou usar uma nova? (Nova/Proxima)").upper()
         if pergunta3 == "PROXIMA":
            numero_t = numero_t + 1
         elif pergunta3 == "NOVA":
            numero_t = int(input("Digite o novo numero: "))