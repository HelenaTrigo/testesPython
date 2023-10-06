# Tarefa G3

# Ex.1 - Helena Trigo

num1 = float(input("Insira o 1º número: \n"))
num2 = float(input("Insira o 2º número: \n"))
num3 = float(input("Insira o 3º número: \n"))
num4 = float(input("Insira o 4º número: \n"))
num5 = float(input("Insira o 5º número: \n"))
num6 = float(input("Insira o 6º número: \n"))
num7 = float(input("Insira o 7º número: \n"))
media = (num1 + num2 + num3 + num4 + num5 + num6 + num7) / 7

print(F"A média dos números inseridos é: {media:.2f}")

# Ex. 2 - Irina

peso = float(input("Qual o peso em kg do utilizador?\n"))
altura = float(input("Qual altura em metros do utilizador?\n"))
imc = peso / altura ** 2

print(F"IMC: {imc:.4f}")

# Ex. 5 - José

numero = int(input("Digite um número: \n"))
sucessor = numero + 1
antecessor = numero - 1

print(
      F"O sucessor de {numero} é {sucessor}\n"
      F"O antecessor de {numero} é {antecessor}"
)

# Ex. 6 - Jennifer

preco = float(input("Valor do produto: \n"))
com_desconto = preco * 0.9

print(
      F"Preço original do produto: EUR {preco:.2f}\n"
      F"Preço com 10% de desconto: EUR {com_desconto:.2f}"
)