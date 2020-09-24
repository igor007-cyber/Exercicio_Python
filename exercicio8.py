"""
8) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
   Calcule e mostre o total do seu salário no referido mês.
"""

ganho_hora = float(input("digite o ganho por hora: "))
numero_horas = float(input("digite somente o numero de horas de trabalho: "))

print("meses que vai ate dia 31: ", ganho_hora * numero_horas * 31)
print("meses que vai ate dia 30: ", ganho_hora * numero_horas * 30)
print("fevereiro ate dia 28: ", ganho_hora * numero_horas * 28)
print("fevereiro ate dia 29: ", ganho_hora * numero_horas * 29)