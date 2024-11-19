print("="*50)
print("Bem vindo ao nosso sistema de cadastro!")
print("="*50)
login = input("Digite seu Login: ")
senha = input("Digite sua senha: ")
senha_2 = input("Confirme a sua senha: ")
while senha_2 != senha:
    print("Senha errada, digite novamente")
    senha_2 = input("Confirme sua senha: ") 
