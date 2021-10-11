'''

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

'''

letter = input("Digite um letra: ")
qtd = len(letter)

if qtd > 1:
    print("voce digitou de mais")
elif qtd <= 0:
    print('voce nao digitou nada')
elif letter.isnumeric() or letter.isdigit() or letter.isdecimal():
    print("isso é um numero,A digite novamente")
else:
    if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U':
        print(f"a letra {letter} é uma vogal")
    else:
        print(f"a letra {letter} é uma consoante")

