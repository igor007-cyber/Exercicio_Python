'''

3) Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

'''

letra =  input("digite 'F' se voce é feminino ou 'M' se voce é masculino: ")

if letra == 'F' or letra == 'f':
    print("voce é feminino")
elif letra == 'M' or letra == 'm':
    print("voce é masculino")
else:
    print("Sexo Inválido. Digite Novamente")