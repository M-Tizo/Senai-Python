print("Bem-Vindo ao sistema de Senhas")
print("Favor utilize uma senha com 8 caracteres e que tenha ao menos uma letra maiuscula, minuscula e um numero")

senha = str(input("Digite sua senha: "))
confirmação = (input("Confirme sua senha:"))
quantia = len(senha)
while quantia <8:
    print("Senha com menos de 8 caracteres")
    senha = str(input("Digite sua senha: "))
    confirmação = (input("Confirme sua senha:"))
    quantia = len(senha)
maiusculo = senha.isupper()
while maiusculo == True:
    print("Precisa de um caracter minusculo")
    senha = str(input("Digite sua senha: "))
    confirmação = (input("Confirme sua senha:"))
    maiusculo = senha.isupper()
minusculo = senha.islower()
while minusculo == True:
    print("Precisa de um caracter maiusculo")
    senha = str(input("Digite sua senha: "))
    confirmação = (input("Confirme sua senha:"))
    minusculo = senha.islower()

while confirmação == str and confirmação == int:
    print("Precisa ter numeros e letras")
    senha = str(input("Digite sua senha: "))
    confirmação = input("Confirme sua senha: ")

if maiusculo == False and minusculo == False and senha == confirmação:
    print("Senha valida")
else:
    print("Senha invalida falta um numero!")
