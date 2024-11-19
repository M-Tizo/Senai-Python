print ("Bem-Vindo ao akinator dos numeros")
print("Pense em um numero de 1-10 e eu vou adivinhar!")
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