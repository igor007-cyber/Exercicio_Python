'''

5) Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

'''

nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))

resu = (nota1 + nota2) / 2

if resu == 10:
    print("Aprovado com Distinção")

elif resu >= 7:
    print("Aprovado")

else:
    print("Reprovado")
