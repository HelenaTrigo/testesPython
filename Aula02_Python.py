
nome = "Pedro"
idade = 37

print("O nome do utilizador é:", nome, "e a idade é", idade, "anos", sep="")
print(F"O nome do utilizador é {nome} e a idade é {idade}anos.", end="")

#ex 6

# dados do cliente
nome = "Helena Trigo"
idade = 32
peso = 53

# apresentação dos dados do cliente
print("Nome:", nome)
print("Idade:", idade)
print("Peso:", peso)
print(F"Chamo-me {nome} tenho {peso}kg e tenho {idade} anos.")

#ex7
num1 = 5.6
num2 = 2

# operações aritméticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

# apresentação dos resultados
print(
    F"O resultado da soma dos dois números é: {soma}.\n"
    F"O resultado da subtração dos dois números é: {subtracao:.2f}.\n"
    F"O resultado da multiplicação dos dois números é: {multiplicacao}.\n"
    F"O resultado da divisão dos dois números é: {divisao:.2f}."
)

#ex8
num = 555

soma = num + 56
div = num / 56

print(F"{soma}, {div:.2f}")

#ex9

print(85 * ((1 * 3 + 3) / (70 - 8)))
