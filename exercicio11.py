"""
11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    a) o produto do dobro do primeiro com metade do segundo .
    b) a soma do triplo do primeiro com o terceiro.
    c) o terceiro elevado ao cubo.
"""
import math
num1 = int(input("digite um numero inteiro: "))
num2 = int(input("digite um numero inteiro: "))
num3 = int(input("digite um numero real: "))
print("\n")

# a)

print("o produto do dobro do primeiro com metade do segundo: ", (num1*2) * (num2/2))
print("\n")

# b)

print("a soma do triplo do primeiro com o terceiro: ", (num1*3) + num3)
print("\n")

# c)

print("o terceiro elevado ao cubo: ", num3**3)


